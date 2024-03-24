class Node:
    def __init__(self,val):
        self.parent = self
        self.value = val 
        self.rank = 0

def find_set(x):
    if x.parent != x:
        x.parent = find_set(x.parent)
    return x.parent

def union_set(x,y):
    x = x.parent 
    y = y.parent
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def Kruskal(G):
    n = len(G)
    V = [Node(i) for i in range(n)]
    E = []
    M = []
    for v in range(n):
        for w, cost in G[v]:
            if v > w: E.append([v,w,cost])
    E.sort(key = lambda x: x[2])
    for v,w, cost in E:
        if find_set(V[v]) != find_set(V[w]):
            union_set(V[v], V[w]) 
            M.append([v,w,cost])
    return M



G = [
     [[1,1],[4,5],[5,8]],
     [[0,1],[2,3]],
     [[1,3],[3,6],[4,4]],
     [[4,2],[2,6]],
     [[0,5],[2,4],[3,2],[5,7]],
     [[4,7],[0,8]]
     ]

print(Kruskal(G))