def DFS(G,v,vis,A):
    vis[v] = 1 
    for x in G[v]:
        if vis[x] ==0:
            DFS(G,x,vis,A) 
    A.append(v)

def remake(G):
    n = len(G)
    G2 = [[] for _ in range(n)]
    for i in range(n):
        for x in G[i]:
            G2[x].append(i)

    return G2

def DFS2(G,v,vis,S,idx):
    vis[v] = idx
    for x in G[v]:
        if vis[x] ==-1:
            S[idx].append(x)
            DFS2(G,x,vis,S,idx) 

def silnie(G):
    n = len(G) 
    A = [] 
    vis = [0]*n
    DFS(G,0,vis,A)
    #print(A)
    G2 = remake(G)
    #print(G2)
    idx = 0 
    vis = [-1]*n 
    S = []
    A.reverse()
    for x in A:
        if vis[x] == -1:
            S.append([x])
            DFS2(G2,x,vis,S,idx)
            idx += 1
    return S


G = [[1],[2],[0,3,7],[4,6],[5],[3],[5],[8],[5,9],[3,10],[7]]
print(silnie(G))