from math import inf 
import heapq 

def MST_Prim(G):
    n = len(G)
    dist = [inf]*n
    parent = [None]*n
    Q = []
    dist[0] = 0
    heapq.heappush(Q,(0,0))
    while Q:
        cost, v = heapq.heappop(Q)
        for x, w in G[v]:
            if dist[x] > w and x != parent[v]:
                dist[x] = w 
                heapq.heappush(Q,(w,x))
                parent[x] = v
    print(parent)
    print(dist)
    return sum(dist)


G = [
     [[1,1],[4,5],[5,8]],
     [[0,1],[2,3]],
     [[1,3],[3,6],[4,4]],
     [[4,2],[2,6]],
     [[0,5],[2,4],[3,2],[5,7]],
     [[4,7],[0,8]]
     ]


print(MST_Prim(G))