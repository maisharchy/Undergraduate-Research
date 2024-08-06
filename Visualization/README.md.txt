# Visualization of CodeConceptNet

## Overview

This part of the project focuses on Visualization for Agglomerative Hierarchical Clustering and a Flask application for interaction with the clustered data.

## Features

- **Dynamic Clustering**: Uses agglomerative clustering to organize data into hierarchical clusters.
- **Interactive Visualization**: Allows users to explore the hierarchical structure of clusters.
- **Flask Application**: A web interface for viewing and interacting with the clustered data.

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**:
   git clone https://github.com/maisharchy/Undergraduate-Research.git
   cd Undergraduate-Research/Visualization

2. **Install Dependencies**:
   Use the provided requirements.txt file to install necessary Python packages.
   pip install -r requirements.txt

## Usage

1. **Running the Flask App**:
   Start the Flask server by executing the main script.
   python app1.py
   The application will be accessible at http://localhost:5000.

2. **Visualizing Clusters**:
   The linkage matrix from the model is used to display hierarchical clustering. The processed data points and vocabulary are also utilized for analysis and visualization.

## Files

- app1.py: Main Flask application script.
- requirements.txt: Lists all the dependencies required for the project.
- linkage_matrix_from_model.pkl: Contains the linkage matrix used for hierarchical clustering.
- processed-point.npy: Processed data points for clustering.
- processed-vocab.npy: Processed vocabulary data for clustering.
- model-500-agglomerative-clustering.pkl: The trained agglomerative clustering model.