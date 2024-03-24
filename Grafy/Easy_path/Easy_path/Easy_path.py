from collections import deque

def BFS(G,v):
    n = len(G)
    dist = [0]*n
    vis = [0]*n
    Q = deque()
    Q.append(v)
    maxi_d = maxi_v = -1
    dist[v] = 0

    w = None
    while len(G[v]) <=2 and vis[v] == 0:
        vis[v] = 1
        for i in G[v]:
            if len(G[i]) <=2 and vis[i] == 0:
                w = i
        dist[w] = dist[v] +1
        v,w = w ,v 
    return dist[w]


def Easy_path(G):
    n = len(G)
    maxi = 0
    for i in range(n):
        maxi = max(maxi,BFS(G,i))
       

G = [
    [1],
    [0],    
    ]

Easy_path(G)