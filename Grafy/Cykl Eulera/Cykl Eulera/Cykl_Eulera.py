

def cycle(G):
    n = len(G) 
    w = [-1]*n 
    vis = [[0 for _ in range(n)] for _ in range(n)]
    res = []
    def DFS(G,v,w,vis):
        nonlocal res
        while w[v] < len(G[v])-1:
            if len(G[v])%2 == 1:
                return None
            w[v] += 1
            x = G[v][w[v]]
            if vis[x][v] == 0 and vis[v][x] == 0:
                vis[x][v] = 1
                vis[v][x] = 1
                DFS(G,x,w,vis)            
        res.append(v)
    DFS(G,0,w,vis)
    for i in w:
       if i == -1: return None
    res.reverse()
    return res


G = [[1,5],[0,2,3,4,5,6],[1,3,4,5],[1,2,4,5],[1,2,3,5],[0,1,2,3,4,6],[1,5]]
G1 = [[1, 1, 4], [3, 0, 1, 2, 4], [1, 3], [0, 4], [2, 0, 4, 1]]
print(cycle(G))
