import time
import tracemalloc

def dfs(adj, dp, src, par):
    for child in adj[src]:
        if child != par:
            dfs(adj, dp, child, src)

    for child in adj[src]:
        if child != par:
            # not including source in the vertex cover
            dp[src][0] = dp[child][1] + dp[src][0]
 
            # including source in the vertex cover
            dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])
    
def vertex_cover_dp(adj):
    tracemalloc.start()
    begin = time.time()
    
    N = adj.number_of_nodes()
    dp = [[0 for j in range(2)] for i in range(N+1)]
    for i in range(1, N+1):
        # 0 denotes not included in vertex cover
        dp[i][0] = 0
 
        # 1 denotes included in vertex cover
        dp[i][1] = 1
    
    dfs(adj, dp, 1, -1)
    
    # printing minimum size vertex cover
    print("Solusi DP:", min(dp[1][0], dp[1][1]))

    end = time.time()
    difference = end - begin
    print(f"Total runtime of the DP program is {difference:.4f} s")

    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Total memory usage of the DP program is {(peak_memory/10**6):.4f} MB")