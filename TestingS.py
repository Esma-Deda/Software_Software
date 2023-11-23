# Import the necessary libraries.
import unittest
import pandas as pd
import networkx as nx
import logging
import requests

from TheCodeS import (
    fetch_protein_interaction_graph,
    create_protein_interaction_graph,
    save_interaction_graph_gml,
    plot_interaction_graph,
)

# Set up logging during testing
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

class TestFetchProteinInteractionGraph(unittest.TestCase):
    """
    Test cases for the `fetch_protein_interaction_graph` function, 
    which retrieves protein interaction data from an external source.
    """
    
    def test_fetch_protein_interaction_graph(self):
        """
        Test the `fetch_protein_interaction_graph` function for different scenarios:
        1. A successful Data Retrieval.
        2. Data Availability and Validity.
        3. Ensure that it contains the necessary columns.
        4. Test if the data contains only the specified proteins.
        """
        try:
            # Fetch the protein interaction data for the specified proteins.
            interaction_data = fetch_protein_interaction_graph(['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2'])
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

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

        # Define a list of two protein names.
        proteins_to_test = ['BRCA1', 'BRCA2']
        # Fetch the protein interaction data for the specified proteins.
        interaction_data = fetch_protein_interaction_graph(proteins_to_test)
         # Check if the fetched data is not None, indicating that the data was successfully retrieved.
        self.assertIsNotNone(interaction_data)
        # Check if the number of rows in the interaction data is greater than 0, ensuring it's not empty.
        self.assertTrue(interaction_data.shape[0] > 0)
        # Check if the DataFrame contains only the specified proteins.
        proteins_in_data = set(interaction_data['preferredName_A']).union(set(interaction_data['preferredName_B']))
        self.assertEqual(set(proteins_to_test), proteins_in_data)
        # Check if specific columns are present in the DataFrame.
        self.assertIn("preferredName_A", interaction_data.columns)
        self.assertIn("preferredName_B", interaction_data.columns)
        self.assertIn("score", interaction_data.columns)


    def test_check_url(self):
        """
        Test to check if the URL is accessible without raising an exception.
        """
        # Define the URL to be checked
        url = 'https://string-db.org/api/tsv/network?'

        # Define the list of proteins
        proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']

        # Add parameters to the request
        params = {
            'identifiers': ','.join(proteins),  
            'species': 9606,  # Human species code
            'required_score': 400,  # Minimum interaction score
            'caller_identity': 'TheCodeS.py'  # Identify the caller
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an HTTP Error for bad responses
        except requests.exceptions.RequestException as e:
            # Log the error and raise an exception
            logging.error(f"An unexpected error occurred while checking the URL: {e}")
            raise

        # Check if the response status code is 200, indicating a successful request
        self.assertEqual(response.status_code, 200, "URL is not accessible") # HTTP status code 200 is the standard response for a successful HTTP request. 



class TestCreateProteinInteractionGraph(unittest.TestCase):
    """
    Test cases for the `create_protein_interaction_graph` function,
    which creates a NetworkX graph from protein interaction data.
    """

    def test_create_protein_interaction_graph(self):
        """
        Tests the creation of the protein interaction graph.
        """
        try:
            # Create a protein interaction graph using the defined or fetched data.
            sample_data = [
                ['BRCA1', 'BRCA2', 500],
                ['BRCA1', 'ATM', 300],
                ['BRCA2', 'ATM', 200]
            ]
            df = pd.DataFrame(sample_data, columns=['preferredName_A', 'preferredName_B', 'score'])
            G = create_protein_interaction_graph(df)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

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
    Test cases for the `save_interaction_graph_gml` function,
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

        try:
            # Call the function to save the graph in GML format
            save_interaction_graph_gml(self.G, self.test_filename)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

        # Call the function to save the graph in GML format
        save_interaction_graph_gml(self.G, self.test_filename)

        # Check if the saved file is in GML format
        with open(self.test_filename, 'r') as file:
            file_content = file.read()
            self.assertTrue(file_content.startswith('graph'))

            # Check if specific nodes are present in the file content
            self.assertIn('node', file_content)
            self.assertIn('BRCA1', file_content)
            self.assertIn('BRCA2', file_content)
            self.assertIn('ATM', file_content)

            # Check if specific edges are present in the file content
            self.assertIn('edge', file_content)
            self.assertIn('source 0', file_content)  # Assuming 'BRCA1' is the first node in the list
            self.assertIn('target 1', file_content)  # Assuming 'BRCA2' is the second node in the list
            self.assertIn('target 2', file_content)  # Assuming 'ATM' is the third node in the list
            
class TestPlotInteractionGraph(unittest.TestCase):
    """
    Test cases for the `plot_interaction_graph` function,
    which generates a visual plot of a NetworkX graph.
    """
    def test_plot_interaction_graph(self):
        """
        Test the `plot_interaction_graph` function to ensure the existing nodes in the graph.
        """
        try:
            # Fetch protein interaction data, create a graph, and plot it
            proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']
            interactions = fetch_protein_interaction_graph(proteins)
            G = create_protein_interaction_graph(interactions)
            plot_interaction_graph(G)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

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