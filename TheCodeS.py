#Import all the necessary libraries 

import requests
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetch_protein_interaction_graph(proteins):
    """
    Fetches the protein interaction graph from the STRING-DB API.
    
    Args:
        proteins (list): List of protein names.
        
    Returns:
        pd.DataFrame: DataFrame with interaction information.
    """
    url = 'https://string-db.org/api/tsv/network?'
    params = {
        'identifiers': '%0d'.join(proteins),
        'species': 9606,  # Human species code
        'required_score': 400,   # Minimum interaction score
        'caller_identity': 'TheCodeS.py'  # Identify the caller
    }
    # Send the API request and get the response
    response = requests.get(url, params=params)

    # Process the response data
    data = [line.split('\t') for line in response.content.decode('utf-8').split('\n') if line and line[0] != '#']
    
    # Create a DataFrame from the response data
    df = pd.DataFrame(data[1:-1], columns=data[0]) 
    
    # Extract the relevant columns for interactions
    interactions = df[['preferredName_A', 'preferredName_B', 'score']]

    return df

def create_protein_interaction_graph(df):
    """
    Creates a protein interaction graph from a DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame with interaction information.
        
    Returns:
        nx.Graph: Protein interaction graph.
    """
    G = nx.Graph(name='Protein Interaction Graph')  

    # Iterate over the rows of the DataFrame and add edges to the graph
    for _, interaction in df.iterrows():
        a = interaction['preferredName_A']
        b = interaction['preferredName_B']
        w = float(interaction['score'])  # score as weighted edge where high scores = low weight
        G.add_weighted_edges_from([(a, b, w)])

    return G

def save_interaction_graph_gml(G, filename):
    """
    Saves a protein interaction graph in GML format.
    
    Args:
        G (nx.Graph): Protein interaction graph.
        filename (str): Name of the GML file.
    """
    nx.write_gml(G, filename)

    
def plot_interaction_graph(G):
    """
    Plots the protein interaction graph.
    
    Args:
        G (nx.Graph): Protein interaction graph.
    """
    pos = nx.spring_layout(G)
    plt.figure(figsize=(11, 9), facecolor=[0.7, 0.7, 0.7, 0.4])
    nx.draw_networkx(G, pos=pos, with_labels=True, font_color='white', font_weight='bold', node_color='blue', edge_color='black')
    plt.axis('off')
    plt.savefig('output.png')

# Define the list of proteins
proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']

# Fetch the protein interaction data
interaction_data = fetch_protein_interaction_graph(proteins)

# Create the protein interaction graph
interaction_graph = create_protein_interaction_graph(interaction_data)

# Save the graph in GML format
save_interaction_graph_gml(interaction_graph, "protein_interaction_graph.gml")

# Plot the interaction graph
plot_interaction_graph(interaction_graph)
