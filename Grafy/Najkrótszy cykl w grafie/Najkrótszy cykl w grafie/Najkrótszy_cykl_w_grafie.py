from math import inf

def shortest_cycle(G):
    n = len(G)
    D = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                D[i][j] = G[i][j]
    for v in range(n):
        for x in range(n):
            for y in range(n):
                D[x][y] = min(D[x][y], D[x][v]+D[v][y])
    res = inf
    for i in range(n): 
        res = min(res,D[i][i])

    return res


G = [
    [0,0,0,2,0,0],
    [4,0,0,0,0,0],
    [7,1,0,0,0,4],
    [0,6,3,0,0,0],
    [1,0,0,0,0,3],
    [0,0,0,0,0,0],
    ]

print(shortest_cycle(G))
