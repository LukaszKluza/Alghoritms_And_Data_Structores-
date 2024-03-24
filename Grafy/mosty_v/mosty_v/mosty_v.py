from math import inf

def DFS(G, v, d, par, low):
    time = 0

    def DFS_Visit(G, v, d, par, low):
        nonlocal time
        time += 1
        d[v] = time
        low[v] = time
        for x in G[v]:
            if d[x] != -1:
                if x != par[v]:
                    low[v] = min(d[v], d[x])
            else:
                par[x] = v
                DFS_Visit(G, x, d, par, low)
        for x in G[v]:
            if par[v] != x:
                low[v] = min(low[x], low[v])

    DFS_Visit(G, v, d, par, low)


G = [[1, 3], [0, 2, 3], [1, 4], [0, 1], [2]]

n=5
LOW = [inf] * n
D = [-1]*n 
P = [None]*n 
DFS(G,0,D,P,LOW)
print(LOW)
print(D)