
def cycle(G,v,vis,idx):
    vis[v] = idx
    for x in G[v]:
        if vis[x] == idx:
                return True 
        return cycle(G,x,vis,idx) 
    return False 

def DFS(G,v,A,vis):
    vis[v] = 1
    for x in G[v]:
        if vis[x] == 0:
           DFS(G,x,A,vis)
    A.append(v)


def top_sort(G):
    n = len(G) 
    vis = [0]*n 
    A = []
    for i in range(n):
         if cycle(G,i,vis, i+1):
            return -1
    vis = [0]*n 
    for i in range(n): 
        if vis[i]==0: 
            DFS(G,i,A,vis)
    A.reverse()
    return A

G = [[1,2],[3],[],[4],[6],[6],[]]
G1 = [[2, 3], [0, 2, 3], [3], []]
G2 = [[2],[2],[]]
print(top_sort(G2))
