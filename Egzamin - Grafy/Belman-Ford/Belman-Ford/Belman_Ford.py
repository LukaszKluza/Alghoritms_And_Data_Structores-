from math import inf 

def Belman_Ford(G,s,t):
    n = len(G)
    dist = [inf]*n 
    dist[s] = 0
    for i in range(n):
        for v in range(n):
            for w,cost in G[v]:
                if dist[w] > dist[v] + cost:
                    dist[w] = dist[v] + cost

    for v in range(n):
        for w,cost in G[v]:
            if dist[w] > dist[v] + cost:
                return None
    return dist[t]




G = [
    [[1,6],[2,1]],
    [[3,1]],
    [[1,2],[3,5],[5,9]],
    [[5,2],[4,4]],
    [[1,-19]],
    []
    ]

print(Belman_Ford(G,0,5))