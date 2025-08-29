import networkx as nx
import random

def assign_random_weights(G, min_weight=1, max_weight=5):
    """Assign random weights to all edges in the graph."""
    for u, v in G.edges():
        G.edges[u, v]['weight'] = random.uniform(min_weight, max_weight)

def randomize_edge_directions(G, bidirectional_prob=0.2):
    """
    Convert undirected graph to directed graph with random edge directions.
    bidirectional_prob: probability that an edge is bidirectional
    """
    DG = nx.DiGraph()
    DG.add_nodes_from(G.nodes(data=True))
    for u, v in G.edges():
        if random.random() < bidirectional_prob:
            # Add edges in both directions
            DG.add_edge(u, v, **G.edges[u, v])
            DG.add_edge(v, u, **G.edges[u, v])
        else:
            if random.choice([True, False]):
                DG.add_edge(u, v, **G.edges[u, v])
            else:
                DG.add_edge(v, u, **G.edges[u, v])
    return DG

def add_random_self_loops(G, self_loop_prob=0.1):
    """
    Add self-loops to nodes with a given probability.
    self_loop_prob: probability (0-1) that a node gets a self-loop
    """
    for node in G.nodes():
        if random.random() < self_loop_prob:
            G.add_edge(node, node)

def create_graph(graph_type):
    """Create a graph of the given type."""
    if graph_type == 'watts_strogatz_newman':
        return nx.watts_strogatz_graph(n=20, k=4, p=0.3)
    elif graph_type == 'barabasi_albert':
        return nx.barabasi_albert_graph(n=20, m=2)
    elif graph_type == 'circulant':
        return nx.circulant_graph(15, [1, 3, 5])
    elif graph_type == 'lattice':
        G = nx.grid_2d_graph(4, 5)
        return nx.convert_node_labels_to_integers(G)
    elif graph_type == 'barbell':
        return nx.barbell_graph(10, 3)
    elif graph_type == 'stochastic_block':
        sizes = [10, 10, 10]
        probs = [[0.8, 0.05, 0.02],
                 [0.05, 0.8, 0.05],
                 [0.02, 0.05, 0.8]]
        return nx.stochastic_block_model(sizes, probs)
    elif graph_type == 'erdos_renyi':
        return nx.erdos_renyi_graph(n=20, p=0.2)
    else:
        raise ValueError("Unknown graph type")

def initialize_tokens(G, initial_tokens=5):
    """Initialize all nodes with a given number of tokens."""
    for node in G.nodes():
        G.nodes[node]['tokens'] = initial_tokens
