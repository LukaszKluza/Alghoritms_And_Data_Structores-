def DFS(G,A,vis,v):
    vis[v] = 1
    for x in G[v]:
        if vis[x] == 0:
            DFS(G,A,vis,x)
    A.append(v)

def DFS_2(G,S,v,idx):
    S[v] = idx
    for x in G[v]:
        if S[x] == -1:
            DFS_2(G,S,x,idx)


def scc(G):
    n = len(G)
    vis = [0]*n 
    G2 = [[] for _ in range(n)]
    A = []
    
    for v in range(n):
        for x in G[v]:
            G2[x].append(v)

    for i in range(n):
        if vis[i] == 0:
           DFS(G,A,vis,i)
    A.reverse()
    S = [-1] *n
    idx = 0
    for x in A:
        if S[x] == -1:
            DFS_2(G2,S,x,idx)
            idx += 1
    G3 = [[] for _ in range(idx)]
    for v in range(n):
        for x in G[v]:
            if S[v] != S[x] and ( not S[x] in G3[S[v]]):
                G3[S[v]].append(S[x])
    return G3


G = [
    [1,2],      #0
    [3,4],      #1
    [3,9],      #2
    [0,7,9],    #3
    [6,7],      #4
    [],         #5
    [8],        #6
    [8,9],      #7
    [4,5],      #8
    [10],    #9
    [5,11],     #10
    [9],         #11
    ]

print(scc(G))