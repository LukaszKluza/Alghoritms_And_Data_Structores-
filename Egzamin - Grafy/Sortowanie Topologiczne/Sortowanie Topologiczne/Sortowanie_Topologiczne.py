
def DFS(G,T,vis,v):
    vis[v] = 1 
    for x in G[v]:
        if vis[x] == 0:
            DFS(G,T,vis,x)
    T.append(v)

def cycle(G,v,vis,idx):
    vis[v] = idx
    for x in G[v]:
        if vis[x] == idx:
                return True 
        return cycle(G,x,vis,idx) 
    return False



def top_sort(G):
    n = len(G)
    vis = [0]*n
    T = [] 
    for i in range(n):
        if cycle(G,i,vis,i+1):
            return -1
    vis = [0]*n
    for x in range(n) :
        if vis[x] == 0:
            DFS(G,T,vis,x)
    T.reverse()
    return T

G = [
    [1,2],
    [2,3],
    [],
    [2],
    [5,6],
    [6],
    [],
    [],
    [7]
]

print(top_sort(G))