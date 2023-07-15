# Importing all the required libraries
import requests
import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the list of proteins
proteins = ['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']

# Define the URL for the STRING-DB API
url = 'https://string-db.org/api/tsv/network?'

# Define the parameters for the API request
params = {
    'identifiers': '%0d'.join(proteins),
    'species': 9606,
    'required_score': 400,
    'caller_identity': 'TheCodeS.py'
}

# Send the API request and get the response
response = requests.get(url, params=params)

# Process the response data
data = [line.split('\t') for line in response.content.decode('utf-8').split('\n') if line and line[0] != '#']

# Create a DataFrame from the response data
df = pd.DataFrame(data[1:-1], columns= data[0])

# Extract the relevant columns for interactions
interactions = df[['preferredName_A', 'preferredName_B', 'score']]

# Create an empty graph object
G = nx.DiGraph(name='Protein Interaction Graph')

# Convert the interactions to a numpy array for processing
interactions = np.array(interactions)


# Iterate over the interactions and add edges to the graph
for i in range(len(interactions)):
    interaction = interactions[i]
    a = interaction[0] # first node
    b = interaction[1] # second node
    w = float(interaction[2]) # score as weighted edge where high scores = low weight
    G.add_weighted_edges_from([(a,b,w)])



# Draw the network graph
pos = nx.spring_layout(G)
plt.figure(figsize=(11,9),facecolor=[0.7,0.7,0.7,0.4])
nx.draw_networkx(G, pos=pos, with_labels=True,font_color='white',font_weight='bold',node_color='blue',edge_color='black')

# Compute betweenness centrality for the nodes
bc = nx.betweenness_centrality(G)
def rescale(l,newmin,newmax):
    arr = list(l)
    return [(x-min(arr))/(max(arr)-min(arr))*(newmax-newmin)+newmin for x in arr]
plt.axis('off')

# Save the plot as an image
plt.savefig('output.png')