# Snakefile

# Rule 1: fetch_protein_interaction_graph
rule fetch_protein_interaction_graph:
    """
    Fetches the protein interaction graph from the STRING-DB API.
    """
    input:
        proteins="proteins.txt"
    output:
        graph_gml="protein_interaction_graph.gml"
    params:
        proteins=['BRCA1', 'BRCA2', 'ATM', 'RAD51', 'PALB2']
    script:
        "TheCode.py"

# Rule 2: plot_interaction_graph
rule plot_interaction_graph:
    """
    Plots the protein interaction graph.
    """
    input:
        graph_gml="protein_interaction_graph.gml"
    output:
        plot_png="output.png"
    script:
        "TheCode.py"

# Rule 3: all (Final Output Rule) that define the final output file or target for the workflow
rule all:
    input:
        "output.png"
