class Node:
    def __init__(self,val):
        self.parent = self 
        self.rank = 0 
        self.val = val

def findset(x):
    if x.parent != x:
        x.parent = findset(x.parent) 
    return x.parent 

def union(x,y):
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank:
        y.parent =  x 
    else:
        x.parent = y 
        if x.rank == y.rank:
            y.rank += 1

def cmp(a):
    return a[2]


def MST(E,n):
    A = [] 
    V = [Node(i) for i in range(n)]
    E.sort(key = cmp)
    for e in E:
        v,w,cost = e
        if findset(V[v]) != findset(V[w]):
            union(V[v],V[w]) 
            A+=[e] 
    print("MST:",A)

E = [[0,1,1],[0,4,5],[0,5,8],[1,2,3],[2,4,4],[2,3,6],[3,4,2],[4,5,7]]
MST(E,6)