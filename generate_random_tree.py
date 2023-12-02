import random
import networkx as nx

def generate_random_tree(N_DP, N_BNB):
    # Create an empty graph
    g_dp = nx.Graph()
    g_bnb = nx.Graph()

    # Add vertices
    g_dp.add_nodes_from(range(1, N_DP + 1))
    g_bnb.add_nodes_from(range(1, N_BNB+ 1))

    # Create a list of vertices
    vertices = list(range(2, N_DP + 1))

    # Randomly shuffle the vertices
    random.shuffle(vertices)

    # Connect each vertex to a random parent to form a tree
    for v in vertices:
        parent = random.choice(range(1, v))
        g_dp.add_edge(parent, v)
        if parent <= N_BNB and v <= N_BNB:
            g_bnb.add_edge(parent, v)

    return g_dp, g_bnb
