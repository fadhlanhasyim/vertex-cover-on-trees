from generate_random_tree import *
from vertex_cover_dp import *
from vertex_cover_bnb import *

if __name__ == '__main__':
    sizes = {"small" : (10_000, 75), "medium" : (100_000, 100), "large" : (1_000_000, 125)}
    for size in sizes.keys():
        print(f"PERCOBAAN DATASET {size.upper()}")
        dp_size, bnb_size = sizes[size]
        dp_graph, bnb_graph = generate_random_tree(dp_size, bnb_size)
        vertex_cover_dp(dp_graph)
        vertex_cover_bnb(bnb_graph)
        print()
 