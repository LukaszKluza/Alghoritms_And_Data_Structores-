class Node:
    def __init__(self, val):
        self.parent = self        
        self.val = val 
        self.rank = 0 

def findset(x):
    if x != x.parent:
        x.parent = findset(x.parent)
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
    return a[2]


def MST(E,n):
    A = []
    V = [Node(i) for i in range(n)]
    E.sort(key = cmp)
    for e in E:
        v,w,cost,idx = e 
        if findset(V[v]) != findset(V[w]):
            union(V[v],V[w]) 
            A += [idx] 
    return A

def solve():
    x = input().split()
    n = int(x[0]) 
    m = int(x[1])
    E = []
    for i in range(m):
        x = input().split()
        v = int(x[0]) 
        w = int(x[1])
        cost = int(x[2])
        E.append([v,w,cost,i])
    res = MST(E,n+1)
    for x in res:
        print(x+1)
    return 0
        
solve()