from collections import deque
from copy import deepcopy

def BFS(G,s,t):
    n = len(G)
    vis = [0]*n
    parent = [None]*n
    Q = deque()
    Q.append(s)
    vis[s] = 1
    while Q:
        v = Q.popleft()
        for i in range(n):
            if G[v][i] > 0 and vis[i] == 0:
                Q.append(i)
                vis[i] = 1 
                parent[i] = v
    P = [] 
    if vis[t] == 0:
        return None
    while t != None:
        P.append(t) 
        t = parent[t]
    P.reverse()
    return P

def capacity(G,path):
    mini = G[path[0]][path[1]] 
    for i in range(1, len(path)-1):
        mini = min(mini, G[path[i]][path[i+1]])
    return mini


def update(G, path):
    w = capacity(G,path)
    for i in range(0,len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w


def max_flow(G,s,t):
    n = len(G) 
    G2 = deepcopy(G) 
    flow = 0 
    path = BFS(G2,s,t)
    while path:
        flow += capacity(G2,path)
        update(G2,path) 
        path = BFS(G2,s,t)
    return flow


G = [
    [0,4,0,3,0,0],
    [0,0,2,2,0,0],
    [0,0,0,0,0,4],    
    [0,0,2,0,2,0],
    [0,0,0,0,0,5],
    [0,0,0,0,0,0]
    ]

G2 = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(max_flow(G2,1,11))



