#
def token_exchange_round(G, weighted=False, directed=False):
    """
    Perform one round of token exchange:
    - Each node distributes ALL its tokens equally among its outgoing neighbors.
    - If a node has a self-loop, it keeps a proportional share of its tokens.
    - Ensures the adjacency matrix is row-stochastic.
    """
    transfers = []

    for node in G.nodes():
        tokens = G.nodes[node]['tokens']
        neighbors = list(G.successors(node)) if directed else list(G.neighbors(node))

        if not neighbors or tokens == 0:
            continue

        # Include self-loop in neighbor list if present
        neighbors_with_self = neighbors.copy()
        if G.has_edge(node, node):
            if node not in neighbors_with_self:
                neighbors_with_self.append(node)

        total_neighbors = len(neighbors_with_self)
        share = tokens / total_neighbors  # use float division

        # Schedule token transfers
        for neighbor in neighbors_with_self:
            transfers.append((node, neighbor, share))

        # Node gives away all tokens
        G.nodes[node]['tokens'] = 0.0

    # Apply transfers
    for sender, recipient, amount in transfers:
        G.nodes[recipient]['tokens'] += amount
