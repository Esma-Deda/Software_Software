#Importing all the requested libraries
import pytest
import requests
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def fetch_protein_network_data():
    """
    Fetches protein interaction data from the STRING database using the network API.

    Returns:
        interactions (pd.DataFrame): DataFrame containing protein interaction data.
    """

    proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']
    url = 'https://string-db.org/api/tsv/network?'

    # Set parameters for the API request
    params = {
        'identifiers': '%0d'.join(proteins),
        'species': 9606,
        'required_score': 400,
        'caller_identity': 'TheCodeS.py'
    }

    # Send the request and retrieve the data
    response = requests.get(url, params=params)
    data = [line.split('\t') for line in response.content.decode('utf-8').split('\n') if line and line[0] != '#']
    df = pd.DataFrame(data[1:-1], columns=data[0])
    interactions = df[['preferredName_A', 'preferredName_B', 'score']]
    return interactions

def test_fetch_protein_network_data():

    interactions = fetch_protein_network_data()
    # Check if the returned value is a DataFrame
    assert isinstance(interactions, pd.DataFrame), "Returned value is not a DataFrame"
    assert not interactions.empty, "DataFrame is empty"

    # Check if the required columns are present
    assert "preferredName_A" in interactions.columns, "Column 'preferredName_A' is missing"
    assert "preferredName_B" in interactions.columns, "Column 'preferredName_B' is missing"
    assert "score" in interactions.columns, "Column 'score' is missing"


def create_protein_interaction_graph(interactions):
    """
    Creates a protein interaction graph from the given interactions.

    Args:
        interactions (pd.DataFrame): DataFrame containing protein interaction data.

    Returns:
        G (nx.Graph): Protein interaction graph.
    """
    G = nx.Graph(name='Protein Interaction Graph')
    interactions = np.array(interactions)
    # Add weighted edges to the graph based on the interactions data
    for interaction in interactions:
        a, b, w = interaction
        w = float(w)
        G.add_weighted_edges_from([(a, b, w)])
    return G


def test_protein_network_requests():
    """
    Tests the protein network data retrieval.
    """
    interactions = fetch_protein_network_data()
    assert not interactions.empty


def test_create_protein_interaction_graph():
    """
    Tests the creation of the protein interaction graph.
    """
    interactions = fetch_protein_network_data()
    G = create_protein_interaction_graph(interactions)

    for interaction in interactions.values:
        a, b, w = interaction[0], interaction[1], interaction[2]

        # Check if nodes are present in the graph
        assert a in G.nodes
        assert b in G.nodes

        # Check if edge weights are correct
        assert G[a][b]['weight'] == float(w)

    assert G.name == 'Protein Interaction Graph'


def test_add_nodes_graph():
    """
    Tests the addition of nodes to the graph.
    """
    interactions = fetch_protein_network_data()
    G = create_protein_interaction_graph(interactions)
     # Check if the returned value is an nx.Graph
    assert isinstance(G, nx.Graph), "Returned value is not an nx.Graph"
    
    
    proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']

    # Check if the set of nodes in the graph matches the expected set of proteins 
    assert set(G.nodes()) == set(proteins), "Missing or additional proteins in the graph"
    
    # Check if the number of nodes in the graph matches the expected number of proteins
    assert len(G.nodes()) == len(proteins), "Number of nodes in the graph is incorrect"

    # Check if the graph is not empty
    assert G.number_of_nodes() > 0, "Graph is empty"

    # Check if the graph contains edges (interactions)
    assert G.number_of_edges() > 0, "Graph has no interactions (edges)"


# Run the tests
if __name__ == '__main__':
    pytest.main()