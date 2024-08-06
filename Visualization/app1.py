import os
import pickle
import numpy as np
from flask import Flask, render_template, jsonify, send_file
from collections import defaultdict
import time
from wordcloud import WordCloud
import matplotlib.pyplot as plt

app = Flask(__name__)

def load_pickle(file_path):
    start_time = time.time()
    with open(file_path, 'rb') as file:
        obj = pickle.load(file)
    print(f"Loaded from {file_path} in {time.time() - start_time:.2f} seconds.")
    return obj

def load_npy(file_path):
    start_time = time.time()
    array = np.load(file_path, allow_pickle=True)
    print(f"Array loaded from {file_path} in {time.time() - start_time:.2f} seconds.")
    return array

def initialize():
    global clustering_model, points, vocab, Z, siblings, clusters, all_clusters
    print("Initializing...")
    clustering_model = load_pickle('model-500-agglomerative-clustering.pkl')
    points = load_npy('processed-point.npy')
    vocab = load_npy('processed-vocab.npy')

    # Load the precomputed linkage matrix
    Z = load_pickle('linkage_matrix_from_model.pkl')

    siblings, clusters = find_siblings_and_words(clustering_model, vocab)
    all_clusters = list(map(int, clusters.keys()))  # Convert keys to standard int
    print(f"Initialization complete. Total clusters populated: {len(clusters)}")

def find_siblings_and_words(model, vocab):
    n_samples = len(model.labels_)
    siblings = {}
    clusters = defaultdict(list)

    # Initialize clusters with vocabulary
    for i, label in enumerate(model.labels_):
        clusters[label].append(vocab[i])
        print(f"Cluster {label} initialized with word: {vocab[i]}")

    for i, merge in enumerate(model.children_):
        cluster_id = n_samples + i
        left_child, right_child = merge
        if left_child >= n_samples:
            left_words = siblings[left_child]["words"]
        else:
            left_words = [vocab[left_child]]

        if right_child >= n_samples:
            right_words = siblings[right_child]["words"]
        else:
            right_words = [vocab[right_child]]

        siblings[cluster_id] = {
            "children": list(map(int, merge)),
            "words": left_words + right_words
        }
        # Add merged clusters to clusters dictionary
        clusters[cluster_id].extend(left_words + right_words)
        print(f"Merged cluster {cluster_id} with words: {left_words + right_words}")

    return siblings, clusters

def generate_word_cloud(words, cluster_id):
    # Ensure the static directory exists
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if not os.path.exists(static_dir):
        os.makedirs(static_dir)

    if not words:
        print(f"No words found for cluster {cluster_id}. Cannot generate word cloud.")
        return None

    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(words))
    plt.figure(figsize=(10, 5), facecolor='k')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    wordcloud_image_path = os.path.join(static_dir, f'wordcloud_cluster_{cluster_id}.png')
    plt.savefig(wordcloud_image_path)
    plt.close()
    return wordcloud_image_path

initialize()

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/get_all_clusters')
def get_all_clusters():
    return jsonify({"clusters": all_clusters})

@app.route('/get_siblings/<int:cluster_id>')
def get_siblings(cluster_id):
    print(f"Requested siblings for cluster ID: {cluster_id}")
    if cluster_id < len(clustering_model.labels_):
        # Initial clusters (data points)
        print(f"Initial cluster {cluster_id} with word: {vocab[cluster_id]}")
        return jsonify([
            {"name": f"Cluster {cluster_id} ({vocab[cluster_id]})"}
        ])
    elif cluster_id in siblings:
        # Merged clusters
        children = siblings[cluster_id]["children"]
        words = siblings[cluster_id]["words"]
        print(f"Cluster {cluster_id} children: {children}, words: {words}")
        return jsonify([
            {"name": f"Cluster {children[0]} ({words[0]})"},
            {"name": f"Cluster {children[1]} ({words[1]})"}
        ])
    else:
        print(f"Cluster {cluster_id} not found in siblings")
        return jsonify([])

@app.route('/get_wordcloud/<int:cluster_id>')
def get_wordcloud(cluster_id):
    print(f"Requested word cloud for cluster ID: {cluster_id}")
    if cluster_id in clusters:
        words = clusters[cluster_id]
        print(f"Words in cluster {cluster_id}: {words}")
        wordcloud_image_path = generate_word_cloud(words, cluster_id)
        if wordcloud_image_path:
            return send_file(wordcloud_image_path, mimetype='image/png')
        else:
            return jsonify({"error": "No words found for this cluster"}), 404
    else:
        print(f"Cluster {cluster_id} not found in clusters")
        return jsonify({"error": "Cluster not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
