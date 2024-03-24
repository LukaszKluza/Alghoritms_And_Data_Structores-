import heapq 
from math import inf 

def MST(G,s):
    n = len(G) 
    Q = []
    A = []
    parent = [None]*n 
    val = [inf]*n 
    val[s] = 0
    vis = [0]*n
    heapq.heappush(Q,(0,s))
    while Q:
        cost, v = heapq.heappop(Q) 
        if vis[v] ==0:
            A.append(v)
            for x,c in G[v]:
                if val[x] > c and vis[x] == 0:
                    val[x] = c 
                    parent[x] = v 
                    heapq.heappush(Q,(c,x)) 
        vis[v] =1
    print(A) 
    print(parent)
    
G = [
    [[1,1],[4,5],[5,8]],
    [[0,1],[2,3]],
    [[1,3],[3,6],[4,4]],
    [[4,2],[2,6]],
    [[0,5],[2,4],[3,2],[5,7]],
    [[4,7],[0,8]]
    ]
MST(G,2)
