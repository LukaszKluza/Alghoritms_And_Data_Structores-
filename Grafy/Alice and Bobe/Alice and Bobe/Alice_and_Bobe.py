from math import inf
import heapq


def Djikstra(G,dist,start,who):
    Q = [] 
    heapq.heappush(Q,(0,start,who))
    while Q:
        cost, v, who = heapq.heappop(Q)
        for x in G[v]:
            if dist[x[0]] > dist[v] + x[1]*who:
                heapq.heappush(Q,(x[1]*(who+1)%2,x[0],(who+1)%2))
                dist[x[0]] = dist[v] + x[1]*who


def Bellman_Ford(G,start,stop):
    n = len(G)
    dist_A = [inf]*n
    dist_A[start] = 0
    Djikstra(G,dist_A,start,1) # 1 = Alice
    dist_B = [inf]*n
    dist_B[start] = 0
    Djikstra(G,dist_B,start,0) # 0 = Bob
    if dist_A[stop] >= dist_B[stop]: #wzracamy kto powinien prowadziæ pierwszy i jaki jest koszt drogi Alice
        return "Bob", dist_B[stop] 
    return "Alice", dist_A[stop]
            

G = [[[1,6],[4,2]],[[2,1],[4,2]],[[3,4]],[[6,7],[7,9]],[[3,5],[5,1]],[[8,3],[9,2]],[],[[10,1]],[[7,3]],[[10,6]],[]]
G2 = [[[1,1],[2,0]],[],[[3,99]],[[4,0],[5,3]],[[1,99]],[]]
print(Bellman_Ford(G,0,10))