# **Protein-Protein Interaction Analysis **

This repository contains Python code for protein interaction analysis using the STRING-DB API and various techniques for testing, object-oriented programming, logging, and workflow management with Snakemake. The code provides a comprehensive solution to fetch protein interaction data, build a protein interaction graph, visualize the graph, and automate the workflow using Snakemake.


## **Code Files**

The repository consists of the following main code files:

1.TheCodeS.py: This file contains the core functions for fetching protein interaction data from the STRING-DB API, building the protein interaction graph, and visualizing the graph using NetworkX and Matplotlib libraries.

2.TestingS.py: This file contains test functions to ensure the correctness and reliability of the protein interaction fetching and graph building processes. The tests are implemented using the pytest framework.

3.OOP.py: This file demonstrates object-oriented programming (OOP) techniques to enhance code modularity and reusability. It defines classes for fetching protein interaction data, building the graph, and visualizing the graph.

4.Snakefile: The Snakemake workflow file automates the entire process of fetching protein interaction data, building the graph, and visualizing the graph using defined rules.

5.LoggingDebugging.py: The file contains code related to logging messages during code execution and providing debugging tools to diagnose and fix issues in the repository's protein interaction data analysis project.


## **Workflow of this repository: The protein interaction analysis workflow consists of the following steps:**

-Fetching Protein Interaction Data: The code fetches protein interaction data from the STRING-DB API based on the list of specified proteins. The data is then processed and stored in a DataFrame.

-Building the Protein Interaction Graph: The fetched protein interaction data is used to construct a weighted graph, where proteins are nodes, and interactions are represented as edges.

-Visualization: The graph is visualized using NetworkX and Matplotlib, producing a plot that showcases the protein interactions.

-Testing: The code includes a testing module with pytest functions to ensure the accuracy of fetching data and building the graph.

-Object-Oriented Programming: The code implements OOP principles by defining classes for the interaction fetching, graph building, and graph visualization processes.

-Snakemake Workflow: The Snakefile defines rules for fetching data and plotting the graph, creating a workflow that automates the entire process.

-Logging and Debugging: The repository incorporates "LoggingDebugging.py," which handles logging messages during code execution and facilitates debugging, ensuring improved reliability and easier issue identification during protein interaction analysis.

## **Usage**

To utilize the code in this repository, follow these steps:

1.Clone the repository:
git clone 'https://github.com/Esma-Deda/Software_Software.git'

2.Install the required librariesusing pip:
pip install -r requirements

3.Explore and use the code files as needed:

a. To fetch protein interaction data and plot the graph, execute "TheCodeS.py" in your preferred Python environment.

b. For testing the correctness of the code, run "TestingS.py" to perform automated tests.

c. If you want to apply object-oriented programming concepts for improved modularity, explore and use "OOP.py" which defines classes for various tasks.

d. If you want to implement logging and debugging features, you can utilize the functionalities provided in "LoggingDebugging.py," which likely contains functions or classes to set up logging configuration, handle messages at different levels (e.g., debug, info, warning, error), and facilitate error tracing during code execution for effective monitoring and issue identification in the protein interaction analysis process.

## **License:**

This repository is provided under the MIT License. You can find the full license in the LICENSE file.


## **Author:**

This repository is maintained by Esma Deda ,esma.deda@studio.unibo.it.

For any questions or inquiries, please contact Esma Deda at esma.deda@studio.unibo.it

## **Contributions and Feedback**

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, please feel free to create pull requests or raise issues.

