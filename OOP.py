# Importing all the request libraries
import requests
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class ProteinInteractionFetcher:
    def __init__(self, proteins):
        """
        Initializes an instance of the ProteinInteractionFetcher class.

        Args:
            proteins (list): List of protein names to fetch interactions for.
        """
        self.proteins = proteins

    def fetch_interactions(self):
        """
        Fetches protein interaction data using the STRING-DB API.

        Returns:
            np.ndarray: Array containing protein interaction data.
        """
        url = 'https://string-db.org/api/tsv/network?'
        params = {
            'identifiers': '%0d'.join(self.proteins),
            'species': 9606,
            'required_score': 400,
            'caller_identity': 'TheCodeS.py'
        }
        response = requests.get(url, params=params)
        data = [line.split('\t') for line in response.content.decode('utf-8').split('\n') if line and line[0] != '#']
        df = pd.DataFrame(data[1:-1], columns=data[0])
        interactions = df[['preferredName_A', 'preferredName_B', 'score']]
        interactions = np.array(interactions)
        return interactions

class ProteinInteractionGraphBuilder:
    def __init__(self):
        """
        Initializes an instance of the ProteinInteractionGraphBuilder class.
        """
        self.G = nx.DiGraph(name='Protein Interaction Graph')

    def build_graph(self, interactions):
        """
        Builds the protein interaction graph from the fetched interactions.

        Args:
            interactions (np.ndarray): Array containing protein interaction data.
        """
        for i in range(len(interactions)):
            interaction = interactions[i]
            a = interaction[0]  # first node
            b = interaction[1]  # second node
            w = float(interaction[2])  # score as weighted edge where high scores = low weight
            self.G.add_weighted_edges_from([(a, b, w)])

class ProteinInteractionGraphVisualizer:
    def __init__(self, graph):
        """
        Initializes an instance of the ProteinInteractionGraphVisualizer class.

        Args:
            graph (nx.DiGraph): The protein interaction graph to visualize.
        """
        self.G = graph

    def visualize_graph(self):
        """
        Visualizes the protein interaction graph.
        """
        pos = nx.spring_layout(self.G)
        plt.figure(figsize=(11, 9), facecolor=[0.7, 0.7, 0.7, 0.4])
        nx.draw_networkx(
            self.G, pos=pos, with_labels=True, font_color='white',
            font_weight='bold', node_color='blue', edge_color='black'
        )
        bc = nx.betweenness_centrality(self.G)
        plt.axis('off')
        plt.savefig('output.png')
