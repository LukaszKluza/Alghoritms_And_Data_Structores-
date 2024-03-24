from math import inf
import heapq

def Djikstra(G,v,dist):
    Q = [] 
    heapq.heappush(Q,(0,v)) 
    dist[v] = 0 
    while Q:
        x,v = heapq.heappop(Q)
        for w,cost in G[v]:
            if dist[w] > dist[v]+cost:
                dist[w] = dist[v]+cost 
                heapq.heappush(Q,(cost,w))
            
    


def solve(G):
    n = len(G) 
    dist1 = [inf for _ in range(n)]
    Djikstra(G,0,dist1)
    maxi = v_maxi = 0
    for i in range(n):
        if dist1[i] < maxi and dist1[i] != 0:
            v_maxi = i 
    dist1 = [inf for _ in range(n)]
    Djikstra(G,v_maxi,dist1) 
    maxi2 = v_maxi2 = 0 
    for i in range(n):
        if dist1[i] > maxi2:
            v_maxi2 = i 
    print(v_maxi, v_maxi2)

G = [
        [[1,4],[2,1]],
        [[0,4],[2,3],[4,7]],
        [[0,1],[1,3],[3,1],[5,2]],
        [[2,1],[5,9],[4,8],[6,3]],
        [[1,7],[6,4],[3,8]],
        [[2,2],[3,9]],
        [[3,3],[4,4]]
    ]

solve(G)
