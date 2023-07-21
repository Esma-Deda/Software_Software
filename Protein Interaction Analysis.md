Protein-Protein Interaction Analysis 

This repository contains Python code for protein interaction analysis using the STRING-DB API and various techniques for testing, object-oriented programming, logging, and workflow management with Snakemake. The code provides a comprehensive solution to fetch protein interaction data, build a protein interaction graph, visualize the graph, and automate the workflow using Snakemake.


Code Files

The repository consists of the following main code files:

1.TheCodeS.py: This file contains the core functions for fetching protein interaction data from the STRING-DB API, building the protein interaction graph, and visualizing the graph using NetworkX and Matplotlib libraries.
2.TestingS.py: This file contains test functions to ensure the correctness and reliability of the protein interaction fetching and graph building processes. The tests are implemented using the pytest framework.
3.OOP.py: This file demonstrates object-oriented programming (OOP) techniques to enhance code modularity and reusability. It defines classes for fetching protein interaction data, building the graph, and visualizing the graph.
4.Snakefile: The Snakemake workflow file automates the entire process of fetching protein interaction data, building the graph, and visualizing the graph using defined rules.

Workflow

The protein interaction analysis workflow consists of the following steps:

1.Fetching Protein Interaction Data: The code fetches protein interaction data from the STRING-DB API based on the list of specified proteins. The data is then processed and stored in a DataFrame.
2.Building the Protein Interaction Graph: The fetched protein interaction data is used to construct a weighted graph, where proteins are nodes, and interactions are represented as edges.
3.Visualization: The graph is visualized using NetworkX and Matplotlib, producing a plot that showcases the protein interactions.
4.Testing: The code includes a testing module with pytest functions to ensure the accuracy of fetching data and building the graph.
5.Object-Oriented Programming: The code implements OOP principles by defining classes for the interaction fetching, graph building, and graph visualization processes.
6.Snakemake Workflow: The Snakefile defines rules for fetching data and plotting the graph, creating a workflow that automates the entire process.


Usage

To utilize the code in this repository, follow these steps:

1.Clone the repository:
git clone 'https://github.com/Esma-Deda/Software.git'

2.Install the required librariesusing pip:
pip install -r requirements

3.Explore and use the code files as needed:
-Execute "TheCodeS.py" to fetch protein interaction data and plot the graph.
-Run "TestingS.py" to ensure the correctness of the code through automated tests.
-Utilize "OOP.py" to apply object-oriented programming concepts for modularity.

4.To automate the workflow using Snakemake, execute the Snakefile:

run : snakemake



Usage:
1.Clone the repository to your local machine using the following command: git clone https://github.com/Esma-Deda/Software_Software/tree/main

2.Install the required libraries by running:
pip install requests networkx pandas numpy matplotlib

3.Execute the analysis by running the main.py script:



Contributing:

Contributions to this repository are welcome! If you find any issues, have suggestions for improvements, or want to add new features, feel free to create a pull request. Please follow the existing code style and include relevant tests for new functionalities.

License:

This repository is provided under the MIT License. You can find the full license in the LICENSE file.

Author:

This repository is maintained by Esma Deda ,esma.deda@studio.unibo.it.

For any questions or inquiries, please contact Esma Deda at esma.deda@studio.unibo.it

Contributions and Feedback

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, please feel free to create pull requests or raise issues.

