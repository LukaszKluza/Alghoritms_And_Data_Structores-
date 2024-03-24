from zad7ktesty import runtests

def DFS(T, n,m, vis, x,y):
    S = [(x,y)]
    vis[x][y] = 1
    cost = 0
    while S:
        x, y = S.pop()
        cost += T[x][y]
        if x - 1 >= 0 and vis[x-1][y] == 0 and T[x-1][y]:
            S.append((x-1,y))
            vis[x-1][y] = 1
        if x + 1 < n and vis[x+1][y] == 0 and T[x+1][y]:
            S.append((x+1,y))
            vis[x+1][y] = 1
        if y - 1 >=0 and vis[x][y-1] == 0 and T[x][y-1]:
            S.append((x,y-1))
            vis[x][y-1] = 1
        if y + 1 < m and vis[x][y+1] == 0 and T[x][y+1]:
            S.append((x,y+1))
            vis[x][y+1] = 1
    return cost

def ogrodnik (T, D, Z, l):
    n = len(T)
    m = len(T[0])
    vis = [[0 for _ in range(m)] for _ in range(n)]
    DP = [[0 for _ in range(l)] for _ in range(len(D)+1)]
    C = []
    for x in D:
        C.append(DFS(T,n,m,vis, 0,x))
    for i in range(1,len(Z)+1):
        value = Z[i-1]
        water = C[i-1]
        for j in range(l):
            if j >= water:DP[i][j] = max(DP[i-1][j],DP[i-1][j-water]+value)
            else: DP[i][j] = DP[i-1][j]
    '''print(C)
    for x in DP:
        print(x)
    '''
    return DP[len(D)][l-1]


runtests( ogrodnik, all_tests=True )
