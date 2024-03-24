from zad6testy import runtests
from math import inf
from collections import deque


def BFS(G, s, t):
    n = len(G)
    parent = [None]*n
    vis = [0]*n
    vis[s] = 1
    Q = deque()
    Q.append(s)
    while Q:
        v = Q.popleft()
        if (v == t):
            break
        for i in range(n):
            if G[v][i] > 0 and vis[i] == 0:
                Q.append(i)
                vis[i] = 1
                parent[i] = v
                if (i == t):
                    break
    Path = []
    if vis[t] == 0:
        return None
    while t != None:
        Path.append(t)
        t = parent[t]
    Path.reverse()
    return Path

def DFS(G, s, t):
    n = len(G)
    parent = [None]*n
    vis = [0]*n
    vis[s] = 1
    Q = []
    Q.append(s)
    while Q:
        v = Q.pop()
        #print(v)
        if(v == t):
            break
        for i in range(n):
            if G[v][i] > 0 and vis[i] == 0:
                Q.append(i)
                vis[i] = 1
                parent[i] = v
                if i == t:
                    break
    Path = []
    if vis[t] == 0:
        return None
    while t != None:
        Path.append(t)
        t = parent[t]
    Path.reverse()
    return Path


def capacity(G, path):
    mini = G[path[0]][path[1]]
    for i in range(1, len(path)-1):
        mini = min(mini, G[path[i]][path[i+1]])
    return mini

def update(G, path):
    w = capacity(G, path)
    for i in range(0, len(path)-1):
        G[path[i]][path[i+1]] -= w
        G[path[i+1]][path[i]] += w

def max_flow(G, s, t):
    n = len(G)
    path = BFS(G, s, t)
    flow = 0
    while path:
        #print(path)
        flow += capacity(G, path)
        update(G, path)
        path = BFS(G, s, t)
    return flow

def binworker( M ):
    # 2*n-2 źródło, 2*n-1 ujście
    n = len(M)
    G = [[0 for _ in range(2*n+2)] for _ in range(2*n+2)]
    for i in range(n):
        for v in M[i]:
            G[i+n][v] = 1

    for i in range(n):
        G[i][2*n+1] = 1
        G[2*n][n+i] = 1

    #for x in G:
    #    print(x)
    res = max_flow(G, 2*n, 2*n+1)
    #print("Res ",res)
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )

M = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ]

#binworker(M)