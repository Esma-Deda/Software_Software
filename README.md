# **Protein-Protein Interaction Analysis**

This repository contains Python code for protein interaction analysis using the STRING-DB API and various techniques for testing, object-oriented programming, logging, and workflow management with Snakemake. The code provides a comprehensive solution to fetch protein interaction data, build a protein interaction graph, visualize the graph, and automate the workflow using Snakemake.

## **Code Files**
The repository consists of the following main code files:

1.TheCodeS.py: This file contains the core functions for fetching protein interaction data from the STRING-DB API, building the protein interaction graph, and visualizing the graph using NetworkX and Matplotlib libraries.

2.TestingS.py: This file contains test functions to ensure the correctness and reliability of the protein interaction fetching and graph building processes. The tests are implemented using the pytest framework.

3.OOP.py: This file demonstrates object-oriented programming (OOP) techniques to enhance code modularity and reusability. It defines classes for fetching protein interaction data, building the graph, and visualizing the graph.

4.Snakefile: The Snakemake workflow file automates the entire process of fetching protein interaction data, building the graph, and visualizing the graph using defined rules.

5.LoggingDebugging.py: The file contains code related to logging messages during code execution and providing debugging tools to diagnose and fix issues in the repository's protein interaction data analysis project.


## **Installation Instructions**

To run this repository, follow these steps:

### Prerequisites
- Python 3.x
- Required Python libraries (install via pip):
  - requests
  - networkx
  - pandas
  - numpy
  - matplotlib

### Installation
1. Clone this GitHub repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/protein-interaction-analysis.git

2. Navigate to the project directory:

   cd protein-interaction-analysis

3. Run the code by executing the following command:
    python TheCodeS.py

4. View the results in the 'output.png' image file.


## **Data Resources**

The codes uses the STRING-DB API to fetch protein interaction data. You can find more information about the API here: STRING-DB API Documentation.

## **Code Structure**

The code is structured into classes to handle different aspects of the analysis. Here's an overview:

ProteinInteractionFetcher:
    -Fetches protein interaction data from the STRING-DB API.
ProteinInteractionGraphBuilder:
    -Constructs the protein interaction graph from the fetched data.
ProteinInteractionGraphVisualizer:
    -Visualizes the protein interaction graph and saves it as an image.
Logging:
    -The project uses the Python logging module to capture and log events and errors during execution. Log messages are saved in the "debug.log" file.
Error Handling:
    -The code incorporates error handling with try-except blocks to capture and log errors gracefully.


## **License:**

This repository is provided under the MIT License. You can find the full license in the LICENSE file.


## **Author:**

This repository is maintained by Esma Deda ,
(esma.deda@studio.unibo.it.)

For any questions or inquiries, please contact Esma Deda at (esma.deda@studio.unibo.it)

## **Contributions and Feedback**

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, please feel free to create pull requests or raise issues.

