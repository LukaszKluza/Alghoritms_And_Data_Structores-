from math import inf


def Floyd_warshall(G,s,t):
    n = len(G)
    dist = [[inf for i in range(n)] for _ in range(n)]
    for v in range(n):
        for w,cost in G[v]:
            dist[v][w] = cost

    for i in range(n):
        for x in range(n):
            for v in range(n):
                if dist[x][v] > dist[x][i] + dist[i][v]:
                    dist[x][v] = dist[x][i] + dist[i][v] 
                    
    return dist[s][t]

G = [
    [[1,6],[2,1]],
    [[3,1]],
    [[1,2],[3,5],[5,9]],
    [[5,2],[4,4]],
    [],
    []
    ]


print(Floyd_warshall(G,0,5))