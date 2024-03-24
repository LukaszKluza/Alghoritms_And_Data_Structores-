from math import inf
import heapq 

def Djikstra(G,s,t):
    n = len(G)
    dist = [inf]*n
    Q = []
    heapq.heappush(Q,[0,s])
    dist[s] = 0
    while Q:
        cost, v = heapq.heappop(Q)
        for x, w in G[v]:
            if dist[x] > dist[v] + w:
                dist[x] = dist[v] + w
                heapq.heappush(Q,[w, x])
    return dist[t]

G = [
    [[1,6],[2,1]],
    [[3,1]],
    [[1,2],[3,5],[5,9]],
    [[5,2],[4,4]],
    [],
    []
    ]

print(Djikstra(G,0,5))

