from zad8testy import runtests
import heapq

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
    res = 0
    for x in range(m):
        if T[0][x] and Vis[0][x] == 0:
            F[x] = count_fuel(0,x,T,Vis)
    Q = []
    sum = 0
    maxi = 0
    for i in range(m-1):
        if F[i]:
            heapq.heappush(Q,-F[i])
        if sum == 0:
            res +=1
            temp = heapq.heappop(Q)
            sum-=temp
        sum -= 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

