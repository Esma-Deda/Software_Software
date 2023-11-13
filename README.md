# **Protein-Protein Interaction Analysis**

This repository contains Python code for protein interaction analysis using the STRING-DB API and various techniques for testing,  logging, and workflow management with Snakemake. The code provides a comprehensive solution to fetch protein interaction data, build a protein interaction graph, visualize the graph, and automate the workflow using Snakemake.

## **Installation Instructions**

To run this repository, follow these steps:

### Prerequisites
- Python 3.10.12
- Required Python libraries (install via pip):
  - requests
  - networkx
  - pandas
  - numpy
  - matplotlib

### Installation
1. Clone this GitHub repository to your local machine:
   ```bash
   git clone https://github.com/Esma-Deda/Software_Software.git

2. Navigate to the project directory:

   cd protein-interaction-analysis

3. Run the code by executing the following command:
    python TheCodeS.py

4. View the results in the 'output.png' image file.


## **Code Files**
The repository consists of the following main code files:

1.TheCodeS.py: This file contains the core functions for fetching protein interaction data from the STRING-DB API, building the protein interaction graph, and visualizing the graph using NetworkX and Matplotlib libraries.

2.TestingS.py: This file contains test functions to ensure the correctness and reliability of the protein interaction fetching and graph building processes. The tests are implemented using the pytest framework.

3.Snakefile: The Snakemake workflow file automates the entire process of fetching protein interaction data, building the graph, and visualizing the graph using defined rules.


## **Data Resources**

The codes uses the STRING-DB API to fetch protein interaction data. You can find more information about the API here: STRING-DB API Documentation.

## **Code Structure**

The code is organized into classes to manage different aspects of the analysis. Here's a high-level overview:

### ProteinInteractionFetcher
- **Description:** Fetches protein interaction data from the STRING-DB API.

### ProteinInteractionGraphBuilder
- **Description:** Constructs the protein interaction graph from the fetched data.

### ProteinInteractionGraphVisualizer
- **Description:** Visualizes the protein interaction graph and saves it as an image.

### Logging
- **Description:** The project employs the Python logging module to capture and log events and errors during execution. Log messages are stored in the "debug.log" file.

### Error Handling
- **Description:** The code includes error handling with try-except blocks to gracefully capture and log errors.



## **License:**

This repository is provided under the MIT License. 


## **Author:**

This repository is maintained by Esma Deda ,
(esma.deda@studio.unibo.it.)

For any questions or inquiries, please contact Esma Deda at (esma.deda@studio.unibo.it)

## **Contributions and Feedback**

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, please feel free to create pull requests or raise issues.

