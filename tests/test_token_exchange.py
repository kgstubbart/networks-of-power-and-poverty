import networkx as nx
from token_exchange import token_exchange_round

def test_single_node_self_loop():
    """
    Test: A single node with a self-loop should retain all its tokens after exchange.
    """
    G = nx.DiGraph()
    G.add_node(0, tokens=10)
    G.add_edge(0, 0)  # self-loop

    token_exchange_round(G, directed=True)

    assert abs(G.nodes[0]['tokens'] - 10) < 1e-6, "Node with self-loop should keep all tokens"

def test_single_node_no_self_loop():
    """
    Test: A single node without a self-loop and no neighbors keeps its tokens.
    """
    G = nx.DiGraph()
    G.add_node(0, tokens=10)

    token_exchange_round(G, directed=True)

    assert abs(G.nodes[0]['tokens'] - 10) < 1e-6, "Node with no neighbors should keep all tokens"

def test_even_distribution_two_neighbors():
    """
    Test: A node with two neighbors should split its tokens evenly.
    """
    G = nx.DiGraph()
    G.add_nodes_from([(0, {'tokens': 10}), (1, {'tokens': 0}), (2, {'tokens': 0})])
    G.add_edges_from([(0, 1), (0, 2)])

    token_exchange_round(G, directed=True)

    assert abs(G.nodes[0]['tokens']) < 1e-6, "Node should give away all tokens"
    assert abs(G.nodes[1]['tokens'] - 5.0) < 1e-6, "Neighbor 1 should get half tokens"
    assert abs(G.nodes[2]['tokens'] - 5.0) < 1e-6, "Neighbor 2 should get half tokens"

def test_even_distribution_with_self_loop():
    """
    Test: A node with two neighbors and a self-loop should split tokens 1/3 each.
    """
    G = nx.DiGraph()
    G.add_nodes_from([(0, {'tokens': 9}), (1, {'tokens': 0}), (2, {'tokens': 0})])
    G.add_edges_from([(0, 1), (0, 2), (0, 0)])  # include self-loop

    token_exchange_round(G, directed=True)

    assert abs(G.nodes[0]['tokens'] - 3.0) < 1e-6, "Node should retain 1/3 of tokens"
    assert abs(G.nodes[1]['tokens'] - 3.0) < 1e-6, "Neighbor 1 should get 1/3 tokens"
    assert abs(G.nodes[2]['tokens'] - 3.0) < 1e-6, "Neighbor 2 should get 1/3 tokens"

def test_total_tokens_conserved():
    """
    Test: Total number of tokens should remain constant after exchange.
    """
    G = nx.DiGraph()
    G.add_nodes_from([(0, {'tokens': 5}), (1, {'tokens': 10}), (2, {'tokens': 15})])
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])

    initial_total = sum(G.nodes[n]['tokens'] for n in G.nodes())
    token_exchange_round(G, directed=True)
    final_total = sum(G.nodes[n]['tokens'] for n in G.nodes())

    assert abs(initial_total - final_total) < 1e-6, "Total tokens should be conserved"
