from generate_random_tree import *
from vertex_cover_dp import *
from vertex_cover_bnb import *


def add_edge(adj, x, y):
    adj[x].append(y)
    adj[y].append(x)

if __name__ == '__main__':
    g = nx.Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g_dp, g_bnb = generate_random_tree(1000, 50)
    # print(random_tree.edges)
    # print(nx.to_dict_of_lists(random_tree))
    print("Size of the smallest vertex cover is (DP)", vertex_cover_dp(g))
    print("Size of the smallest vertex cover is (BnB)", (vertex_cover_bnb(g)))

    # for i in range(50, 100):
    #     random_tree = generate_random_tree(i)
    #     dp = vertex_cover_dp(random_tree)
    #     bnb = vertex_cover_bnb(random_tree)
    #     if dp == bnb:
    #         print('SAMA!!')
    #     else:
    #         print('Beda...')
    #         print(nx.to_dict_of_lists(random_tree))

 