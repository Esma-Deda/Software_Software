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
        proteins="BRCA1 BRCA2 ATM RAD51 PALB2"
    script:
        "TheCodeS.py"

# Rule 2: create_protein_interaction_graph
rule create_protein_interaction_graph:
    """
    Creates the protein interaction graph from the fetched data.
    """
    input:
        graph_data="protein_interaction_graph.gml"  # Change to match the expected input file
    output:
        graph_gml="protein_interaction_graph.gml"
    script:
        "TheCodeS.py"

# Rule 3: plot_interaction_graph
rule plot_interaction_graph:
    """
    Plots the protein interaction graph.
    """
    input:
        graph_gml="protein_interaction_graph.gml"
    output:
        plot_png="output.png"
    script:
        "TheCodeS.py"

# Rule 4: all (Final Output Rule) that defines the final output file or target for the workflow
rule all:
    input:
        "output.png"
