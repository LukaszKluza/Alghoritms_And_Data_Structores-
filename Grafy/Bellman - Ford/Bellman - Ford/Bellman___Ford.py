from math import inf

def Bellman_Ford(G,v):
    n = len(G)
    dist = [inf]*n
    dist[v] = 0
    for _ in range(n-1):
        for i in range(n):
            for x in G[i]:
                if dist[x[0]] > dist[i] + x[1]:
                    dist[x[0]] = dist[i] + x[1]
    for i in range(n):
        for x in G[i]:
            if dist[x[0]] > dist[i] + x[1]:
                print("Ujemny Cykl")
    return dist
            


G = [[[1,6],[4,2]],[[2,1],[4,2]],[[3,4]],[[6,7],[7,9]],[[3,5],[5,1]],[[8,3],[9,2]],[],[[10,1]],[[7,3]],[[9,6]],[]]
Bellman_Ford(G,0)