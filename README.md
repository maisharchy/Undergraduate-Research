
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

  ### Code Files:

- **`newGui.py`**: This Python file is likely the main script that implements the GUI tool for labeling clusters, utilizing Tkinter. It handles the loading of clusters, user input for lexicographic, syntactic, and semantic labeling, and navigation between clusters.

### Data Files (JSON):

- **`1-50.json`**, **`51-100.json`**, **`101-150.json`**, **`151-200.json`**, **`201-250.json`**, **`251-300.json`**, **`301-350.json`**, **`351-400.json`**, **`401-450.json`**, **`451-500.json`**: These JSON files contain clusters of data, divided by the number ranges in their filenames. Each file stores the cluster information, including tokens, sentence contexts, and possibly user annotations. These files are used by the GUI tool for displaying and labeling clusters.

- **`CodeConceptNet-v1.json`**: This JSON file is just a combined version of all the previous data files 1-500 (without LLM evaluatioin labels) 

- **`one.json`**: This JSON file is a combined version of all the previous data files 1-500 (with LLM evaluation labels) 

### Labeling Files:

- **`codetest2_test_unique.in`**: This file could be an input file which contains code tokens. It is used in conjunction with the labeling tasks. It is not used in the GUI tool. 

- **`codetest2_test_unique.label`**: This file contains corresponding labels for the tokens in the .in file. It is used by the GUI tool to display or compare the assigned labels during the labeling process.

### Documentation:

- **`README.md`**: The main documentation file for the project. It provides an overview of the project, instructions on how to run the GUI tool, and details about how the labeling process works.

### Visualization:

- **`Visualization/`**: This directory contains files related to visualizing the clusters or the results of the labeling process. It may include scripts, data, or other resources for generating visual representations of the clusters.


