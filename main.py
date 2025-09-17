from graph_utils import (
    create_graph,
    initialize_tokens,
    assign_random_weights,
    randomize_edge_directions,
    add_random_self_loops
)
from visualization import draw_graph
from token_exchange import token_exchange_round
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    graph_types = [
        # Small-world network with local clustering and random shortcuts
        'watts_strogatz_newman', 
        
        # Scale-free network, few hubs with many connections
        'barabasi_albert',

        # Each node connects to fixed neighbors in a ring
        'circulant',

        # Regular grid, each node connects to adjacent nodes
        'lattice',

        # Two cliques joined by a bridge of nodes
        'barbell',

        # Communities with dense internal and sparse external connections
        'stochastic_block',

        # Random graph, edges placed independently with fixed probability
        'erdos_renyi'
    ]
    layouts = ['circular', 'spring']

    print("Available graph types:")
    for i, g in enumerate(graph_types):
        print(f"{i}: {g}")
    g_index = int(input("Enter the number of the graph type you want: "))

    print("\nAvailable layouts:")
    for i, layout in enumerate(layouts):
        print(f"{i}: {layout}")
    l_index = int(input("Enter the number of the layout you want: "))

    selected_graph_type = graph_types[g_index]
    selected_layout = layouts[l_index]

    print("\nEnable directed edges?")
    print("0: Undirected graph")
    print("1: Directed graph with random edge directions")
    directed_choice = int(input("Enter choice: "))
    directed = (directed_choice == 1)

    print("\nEnable weighted edges?")
    print("0: Unweighted graph")
    print("1: Weighted graph")
    weighted_choice = int(input("Enter choice: "))
    weighted = (weighted_choice == 1)

    print("\nEnable simple mode (smaller graph)?")
    print("0: No (default size)")
    print("1: Yes (smaller graph, 7-10 nodes)")
    simple_choice = int(input("Enter choice: ") or "0")
    simple_mode = (simple_choice == 1)

    G = create_graph(selected_graph_type, simple=simple_mode)
    initialize_tokens(G, initial_tokens=5)

    self_loop_prob = float(input("\nEnter probability (0-1) of adding self-loops to nodes (default 0.1): ") or "0.1")
    add_random_self_loops(G, self_loop_prob=self_loop_prob)

    if directed:
        bidirectional_prob = float(input("\nEnter probability (0-1) that an edge is bidirectional (default 0.2): ") or "0.2")
        G = randomize_edge_directions(G, bidirectional_prob=bidirectional_prob)

    if weighted:
        assign_random_weights(G, min_weight=1, max_weight=5)

    # Apply layouts with more spacing
    if selected_layout == 'circular':
        pos = nx.circular_layout(G, scale=2.0)
    else:
        pos = nx.spring_layout(G, seed=42, k=1.5, scale=2.0)

    rounds = int(input("\nEnter number of token exchange rounds to run: "))

    print("\nChoose mode:")
    print("0: Animated (auto-advance each round)")
    print("1: Step-through (press Enter for each round)")
    mode = int(input("Enter mode number: "))
    step_through = (mode == 1)

    plt.ion()
    fig = plt.figure(figsize=(8, 6))

    for r in range(rounds):
        token_exchange_round(
            G,
            weighted=weighted,
            directed=directed
        )
        draw_graph(G, pos, title=f'{selected_graph_type} - Round {r+1}', directed=directed)

        if step_through:
            input("Press Enter for next round...")

    plt.ioff()
    plt.show()
    print("\nToken exchange complete!")
