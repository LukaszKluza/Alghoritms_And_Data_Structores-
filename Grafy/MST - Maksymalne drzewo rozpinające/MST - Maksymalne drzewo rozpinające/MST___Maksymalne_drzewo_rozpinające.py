class Node:
    def __init__(self,val):
        self.val = val
        self.parent = self 
        self.rank = 0 


def findset(x):
    if x.parent != x:
        return findset(x.parent)
    return x.parent 

def union(x,y):
    x = findset(x)
    y = findset(y)
    if x.rank > y.rank:
        y.parent = x 
    else:
        x.parent = y 
        if x.rank == y.rank:
            y.rank += 1 

def cmp(a):
    return -a[2]


def MAX_TREE(E,n):
    V = [Node(i) for i in range(n)]
    A = [] 
    res = 0
    E.sort(key=cmp)
    for e in E:
        v,w,cost = e
        if findset(V[v]) != findset(V[w]):
            union(V[v],V[w])
            res += cost
            print(v,w)
    return cost


E = [
    [0,1,4],
    [0,2,1],
    [1,4,7],
    [1,2,3],
    [2,3,1],
    [2,5,2],
    [3,5,9],
    [3,6,3],
    [3,6,3],
    [4,6,4],   
    ]

print(MAX_TREE(E,7))