def DFS(G,vis,v,w,E):
    while w[v] < len(G[v]) -1:
        if len(G[v])%2:
            return None
        w[v]+=1
        x = G[v][w[v]]
        if vis[v][x] == 0 and vis[x][v] == 0:
            vis[v][x] = vis[x][v] = 1
            DFS(G,vis,x,w,E) 
    E.append(v)
        


def Euler(G):
    n = len(G)
    vis = [[0 for _ in range(n)] for _ in range(n)]
    w = [-1]*n
    E = []
    DFS(G,vis,0,w,E)
    E.reverse() 
    return E



G = [[1,5],[0,2,3,4,5,6],[1,3,4,5],[1,2,4,5],[1,2,3,5],[0,1,2,3,4,6],[1,5]]

print(Euler(G))