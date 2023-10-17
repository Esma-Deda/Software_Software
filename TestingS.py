#Import the necessary libraries.
import unittest
import os
import pandas as pd
import networkx as nx
from TheCodeS import (
    fetch_protein_interaction_graph,
    create_protein_interaction_graph,
    save_interaction_graph_gml,
    plot_interaction_graph,
)


class TestFetchProteinInteractionGraph(unittest.TestCase):
    """
    This test case class is used to test the `fetch_protein_interaction_graph` function, 
    which retrieves protein interaction data from an external source.
    """
    
    def test_fetch_protein_interaction_graph(self):
        """
        Test the `fetch_protein_interaction_graph` function for different scenarios:
        1. A successful Data Retrieval.
        2. Data Availability and Validity.
        3. Ensure that it contains the necessary columns.
        """
        # Define a list of protein names.
        proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']
        # Fetch the protein interaction data for the specified proteins.
        interaction_data = fetch_protein_interaction_graph(proteins)
        # Check if the fetched data is not None, indicating that the data was successfully retrieved.
        self.assertIsNotNone(interaction_data)
        # Check if the number of rows in the interaction data is greater than 0, ensuring it's not empty.
        self.assertTrue(interaction_data.shape[0] > 0)
        # Fetch interaction data for the same set of proteins and store it in the 'interactions' variable.
        interactions = fetch_protein_interaction_graph(['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2'])
        # Check if the returned value is a DataFrame.
        assert isinstance(interactions, pd.DataFrame), "Returned value is not a DataFrame"
        # Check if the DataFrame is not empty.
        assert not interactions.empty, "DataFrame is empty"
        # Check if specific columns are present in the DataFrame.
        assert "preferredName_A" in interactions.columns, "Column 'preferredName_A' is missing"
        assert "preferredName_B" in interactions.columns, "Column 'preferredName_B' is missing"
        assert "score" in interactions.columns, "Column 'score' is missing"


class TestCreateProteinInteractionGraph(unittest.TestCase):
    """
    This test case class is used to test the `create_protein_interaction_graph` function,
    which creates a NetworkX graph from protein interaction data.
    """

    def test_create_protein_interaction_graph(self):
        """
        Tests the creation of the protein interaction graph.
        """
        sample_data = [
            ['BRCA1', 'BRCA2', 500],
            ['BRCA1', 'ATM', 300],
            ['BRCA2', 'ATM', 200]
        ]
        df = pd.DataFrame(sample_data, columns=['preferredName_A', 'preferredName_B', 'score'])

        # Create a protein interaction graph using the defined or fetched data.
        G = create_protein_interaction_graph(df)

        for interaction in df.values:
            a, b, w = interaction[0], interaction[1], interaction[2]

            # Check if nodes are present in the graph
            assert a in G.nodes
            assert b in G.nodes
            # Check if edge weights are correct
            assert G[a][b]['weight'] == float(w)

        # Check if the interaction graph has more than 0 nodes, ensuring it's not empty.
        self.assertTrue(G.number_of_nodes() > 0)
        # Check if the interaction graph has more than 0 edges, ensuring it contains interactions.
        self.assertTrue(G.number_of_edges() > 0)
        # Check the name of the graph
        self.assertEqual(G.name, 'Protein Interaction Graph')

class TestSaveInteractionGraphGML(unittest.TestCase):
    """
    This test case class is used to test the `save_interaction_graph_gml` function,
    which saves a NetworkX graph in GML format.
    """
    def setUp(self):
        # Define a sample graph
        self.G = nx.Graph()
        self.G.add_edge('BRCA1', 'BRCA2', weight=500)
        self.G.add_edge('BRCA1', 'ATM', weight=300)
        self.G.add_edge('BRCA2', 'ATM', weight=200)

        # Define the test GML file name
        self.test_filename = 'test_interaction_graph.gml'

    def test_save_interaction_graph_gml(self):
        """
        Test the `save_interaction_graph_gml` function to ensure it saves the graph in GML format.
        """
        # Call the function to save the graph in GML format
        save_interaction_graph_gml(self.G, self.test_filename)
        # Check if the saved file is in GML format
        with open(self.test_filename, 'r') as file:
            file_content = file.read()
            self.assertTrue(file_content.startswith('graph'))

class TestPlotInteractionGraph(unittest.TestCase):
    """
    This test case class is used to test the `plot_interaction_graph` function,
    which generates a visual plot of a NetworkX graph.
    """
    def test_plot_interaction_graph(self):
        """
        Test the `plot_interaction_graph` function to ensure the existing  nodes to the graph.
        """
        proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']
        interactions = fetch_protein_interaction_graph(proteins)
        G = create_protein_interaction_graph(interactions)

        # Check if the returned value is an nx.Graph
        assert isinstance(G, nx.Graph), "Returned value is not an nx.Graph"
        

        # Check if the set of nodes in the graph matches the expected set of proteins 
        assert set(G.nodes()) == set(proteins), "Missing or additional proteins in the graph"

        # Check if the number of nodes in the graph matches the expected number of proteins
        assert len(G.nodes()) == len(proteins), "Number of nodes in the graph is incorrect"

        # Check if the graph is not empty
        assert G.number_of_nodes() > 0, "Graph is empty"

        # Check if the graph contains edges (interactions)
        assert G.number_of_edges() > 0, "Graph has no interactions (edges)"
        
if __name__ == '__main__':
    unittest.main()