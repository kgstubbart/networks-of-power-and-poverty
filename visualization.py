import matplotlib.pyplot as plt
import matplotlib.colors as colors
import networkx as nx
import numpy as np

def draw_graph(G, pos, title='Graph', token_attr='tokens', directed=False):
    """Draw the graph with nodes colored by token count."""
    plt.clf()

    tokens = nx.get_node_attributes(G, token_attr)
    token_values = list(tokens.values())

    min_tokens = min(token_values) if token_values else 0
    max_tokens = max(token_values) if token_values else 1
    if max_tokens == min_tokens:
        max_tokens += 1  # Prevent divide-by-zero

    norm = colors.Normalize(vmin=min_tokens, vmax=max_tokens)
    base_cmap = plt.colormaps['Greens']
    darker_greens = colors.LinearSegmentedColormap.from_list(
        'darker_greens', base_cmap(np.linspace(0.1, 1.0, 256))
    )

    node_colors = [darker_greens(norm(tokens[n])) for n in G.nodes()]
    labels = {node: f'{node}\n{tokens.get(node, 0):.3f} tokens' for node in G.nodes()}

    ax = plt.gca()

    if nx.get_edge_attributes(G, 'weight'):
        edge_weights = [G.edges[u, v]['weight'] for u, v in G.edges()]
        max_width = 5
        min_width = 0.5
        norm_weights = [(w / max(edge_weights)) * (max_width - min_width) + min_width for w in edge_weights]
    else:
        norm_weights = 1

    nx.draw_networkx_edges(G, pos, width=norm_weights, edge_color='gray', arrows=directed, ax=ax)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500, ax=ax)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, ax=ax)

    sm = plt.cm.ScalarMappable(cmap=darker_greens, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, shrink=0.75)
    cbar.set_label('Token Count', rotation=270, labelpad=15)

    ax.set_title(f'{title}')
    plt.pause(0.5)
