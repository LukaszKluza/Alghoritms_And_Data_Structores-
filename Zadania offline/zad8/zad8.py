from zad8testy import runtests
from math import  inf

def count_fuel(x,y, T, Vis):
    n = len(T)
    m = len(T[0])
    Q = []
    sum_fuel = 0
    Q.append([x,y])
    Vis[x][y] = 1
    while(Q):
        x,y = Q.pop()
        sum_fuel += T[x][y]
        if x > 0 and Vis[x-1][y] == 0 and T[x-1][y]:
            Q.append([x-1,y])
            Vis[x - 1][y] = 1
        if y > 0 and Vis[x][y-1] == 0 and T[x][y-1]:
            Q.append([x,y-1])
            Vis[x][y-1] = 1
        if x < n-1 and Vis[x + 1][y] == 0 and T[x+1][y]:
            Q.append([x + 1,y])
            Vis[x + 1][y] = 1
        if y < m-1 and Vis[x][y + 1] == 0 and T[x][y+1]:
            Q.append([x,y + 1])
            Vis[x][y + 1] = 1
    return sum_fuel


def plan(T):
    n = len(T)
    m = len(T[0])
    Vis = [[0 for _ in range(m)] for _ in range(n)]
    F = [0]*m
    DP = [inf]*m
    for x in range(m):
        if T[0][x] and Vis[0][x] == 0:
            F[x] = count_fuel(0,x,T,Vis)
    DP[0] = 0
    for i in range(m):
        if F[i]:
            for j in range(m-1,i,-1):
                if j - F[i] <= 0:
                    DP[j] = min(DP[j],DP[i]+1)
                elif DP[j-F[i]] < inf:
                    DP[j] = min(DP[j], DP[j - F[i]] + 1)
    return DP[m-1]

T = [
    [3,0,0,1,0,3,0,1,0,0,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

