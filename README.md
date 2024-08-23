
# Cluster Labeling Tool

This `Cluster Labeling Tool` is a Python application built with `Tkinter` that helps users label and annotate clusters of words. This tool facilitates user input regarding lexicographic, syntactic, semantic, and descriptive labeling for clusters, and stores the results in a JSON file. The tool also supports navigation through clusters, allowing users to move to the previous or next cluster for labeling.

## Key Features:

- **Cluster Display:** Displays clusters of words and allows users to view the tokens, their labels, and the sentence context from which they are extracted.
- **User Input:** Users can provide inputs for Lexicographic, Syntactic, Semantic, and Descriptive categories for each cluster.
- **Meaningful Cluster Assessment:** Users can indicate whether they find a cluster meaningful through a set of radio buttons.
- **Research Questions:** Users can answer research questions related to the labels produced by ChatGPT and provide feedback on common errors, precision, and label categories.
- **Error Analysis:** A dropdown menu allows users to choose the most applicable error analysis for LLM labeling (e.g., "Sensitive Content Models", "Linguistic Ontologies").
- **JSON File Updates:** The tool stores user inputs and responses back into a JSON file, updating the data with meaningful annotations for further analysis.
- **Navigation:** The user can navigate between clusters using 'Next' and 'Previous' buttons.

## Getting Started

### Prerequisites

To use this tool, ensure you have the following installed:

- Python 3.x
- Tkinter (included with standard Python installations)
- The JSON file containing the clusters (`451-500.json`)
- The labels file (`codetest2_test_unique.label`)

### Installation

1. Clone or download the project to your local machine.
2. Make sure that your JSON file and labels file are in the same directory as the script.
3. Run the script using Python:

   ```bash
   python newGUI.py
   ```

### Usage

1. **Load Data:** When the tool starts, it will automatically load the first cluster of data from the JSON file.
2. **Label Clusters:** Use the input fields to provide your labels and descriptions for the cluster.
3. **Answer Research Questions:** Use the provided dropdown menus and input fields to answer the research questions.
4. **Navigate:** Use the 'Next' and 'Previous' buttons to move through clusters and continue labeling.
5. **Submit Data:** After entering your inputs, click the 'Enter' button to store your responses in the JSON file.
6. **Save:** Your annotations will be automatically saved to the JSON file after each entry.

### Directory Structure

```
├── cluster_labeling_tool.py     # Main script file
├── 451-500.json                 # JSON file containing clusters data
├── codetest2_test_unique.label  # Label file
└── README.md                    # This README file
```

### Customization

You can adjust the following as needed:

- **Cluster Data File:** Update the `json_file_path` variable to point to a different JSON file with cluster data.
- **Labels File:** Update the `labels_file_path` variable to point to a different labels file.

