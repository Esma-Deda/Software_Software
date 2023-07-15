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
        nx.Graph: Protein interaction graph.
    """
    url = 'https://string-db.org/api/tsv/network?'
    params = {
        'identifiers': '%0d'.join(proteins),
        'species': 9606,
        'required_score': 400,
        'caller_identity': 'final_project.py'
    }
    response = requests.get(url, params=params)
    data = [line.split('\t') for line in response.content.decode('utf-8').split('\n') if line and line[0] != '#']
    df = pd.DataFrame(data[1:-1], columns=data[0])
    interactions = df[['preferredName_A', 'preferredName_B', 'score']]
    G = nx.Graph(name='Protein Interaction Graph')
    interactions = np.array(interactions)
    for i in range(len(interactions)):
        interaction = interactions[i]
        a = interaction[0]  # first node
        b = interaction[1]  # second node
        w = float(interaction[2])  # score as weighted edge where high scores = low weight
        G.add_weighted_edges_from([(a, b, w)])
    return G


# Define the list of proteins
proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']

# Fetch the protein interaction graph using the defined function
G = fetch_protein_interaction_graph(proteins)

def plot_interaction_graph(G):
    """
    Plots the protein interaction graph.
    
    Args:
        G (nx.Graph): Protein interaction graph.
    """
    pos = nx.spring_layout(G)
    plt.figure(figsize=(11, 9), facecolor=[0.7, 0.7, 0.7, 0.4])
    nx.draw_networkx(G, pos=pos, with_labels=True, font_color='white', font_weight='bold', node_color='blue', edge_color='black')
    bc = nx.betweenness_centrality(G)
    plt.axis('off')
    plt.savefig('output.png')

# Plot the interaction graph using the defined function
plot_interaction_graph(G)
