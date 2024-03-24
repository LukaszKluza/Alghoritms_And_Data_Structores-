from math import inf

def Bellman_Ford(E,n,s):
    dist = [inf]*n
    dist[s] = 0
    for i in range(n-1):
        for x in E:
            u, v, cost = x
            if dist[v] > dist[u] + cost:
                dist[v] = dist[u] + cost
    for x in E:
            u, v, cost = x
            if dist[v] > dist[u] + cost:
                print("NIE")
                return 
    for i in range(n):
        if i != s: print(i,dist[i]) 
    return 

def solve():
    E = []
    n = m = s = 0
    v = w = cost =  0 
    x = input().split()
    n = int(x[0])
    m = int(x[1])
    s = int(x[2])
    while m > 0:
        x = input().split()
        v = int(x[0])
        w = int(x[1])
        cost = int(x[2])
        E.append((v,w,cost))
        m-=1
    #print(E)
    Bellman_Ford(E,n,s)


solve()
