from math import inf 

time = 0

def DFS(G,v,vis,par,low):
    print(v,vis[v])
    global time
    time += 1 
    vis[v] = time 
    low[v] = time 
    for x in G[v]:
        if vis[x] != -1 and x != par[v]:
            low[v] = min(low[v],vis[x])
        elif vis[x] == -1:
            par[x] = v 
            DFS(G,x,vis,par,low)
            low[v] = min(low[x],low[v])


def mosty(G):
    n = len(G)
    low = [inf]*n
    vis = [-1]*n
    parent = [None]*n
    DFS(G,0,vis,parent, low) 
    for i in range(n):
        if low[i] == vis[i] and parent[i] != None and low[i] != low[parent[i]]:
            print(i,parent[i])
    print(low)
    print(vis)

G = [
    [1,6],
    [0,2],
    [1,3,6],
    [2,4,5],
    [3,5],
    [3,4],
    [0,2,7],
    []
    ]

print(mosty(G))