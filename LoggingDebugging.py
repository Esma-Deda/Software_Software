# Import all the necessary libraries
import requests
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

def fetch_protein_interaction_graph(proteins):
    """
    Fetches the protein interaction graph from the STRING-DB API.
    
    Args:
        proteins (list): List of protein names.
        
    Returns:
        nx.Graph: Protein interaction graph.
    """
    # Define the URL for the STRING-DB API
    url = 'https://string-db.org/api/tsv/network?'
    
    # Define the parameters for the API request
    params = {
        'identifiers': '%0d'.join(proteins),
        'species': 9606,
        'required_score': 400,
        'caller_identity': 'final_project.py'
    }
    
    try:
        # Send the API request and get the response
        response = requests.get(url, params=params)
        response.raise_for_status()
        logging.debug(f"API request URL: {response.url}")
        logging.debug(f"API response status code: {response.status_code}")
        
        # Process the response data
        data = [line.split('\t') for line in response.content.decode('utf-8').split('\n') if line and line[0] != '#']
        df = pd.DataFrame(data[1:-1], columns=data[0])
        interactions = df[['preferredName_A', 'preferredName_B', 'score']]
        
        # Create an empty graph object
        G = nx.Graph(name='Protein Interaction Graph')
        
        # Convert the interactions to a numpy array for processing
        interactions = np.array(interactions)
        
        # Iterate over the interactions and add edges to the graph
        for i in range(len(interactions)):
            interaction = interactions[i]
            a = interaction[0]  # first node
            b = interaction[1]  # second node
            w = float(interaction[2])  # score as weighted edge where high scores = low weight
            G.add_weighted_edges_from([(a, b, w)])
        
        return G
    
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred during the API request: {e}")
        raise

    except Exception as e:
        logging.error(f"An error occurred during data processing: {e}")
        raise

def plot_interaction_graph(G):
    """
    Plots the protein interaction graph.
    
    Args:
        G (nx.Graph): Protein interaction graph.
    """
    try:
        # Draw the network graph
        pos = nx.spring_layout(G)
        plt.figure(figsize=(11, 9), facecolor=[0.7, 0.7, 0.7, 0.4])
        nx.draw_networkx(G, pos=pos, with_labels=True, font_color='white', font_weight='bold', node_color='blue', edge_color='black')
        
        # Compute betweenness centrality for the nodes
        bc = nx.betweenness_centrality(G)
        
        plt.axis('off')
        
        # Save the plot as an image
        plt.savefig('output.png')
        
    except Exception as e:
        logging.error(f"An error occurred during graph plotting: {e}")
        raise

# Define the list of proteins
proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']

try:
    # Fetch the protein interaction graph
    G = fetch_protein_interaction_graph(proteins)
    
    # Plot the interaction graph
    plot_interaction_graph(G)
    
    logging.info("Code execution completed successfully.") 

except Exception as e:
    logging.exception("An unexpected error occurred:")
    raise
