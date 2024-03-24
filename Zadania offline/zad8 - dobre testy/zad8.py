'''Lukasz Kluza
Poczatkowo wykonuje DFS-a na macierzy T, aby zliczyc paliwo i skompersowac to do jednowymiarowej tablicy F,
kolejno urouchamiam algorytm zachlanny, ktory polega na tym ze iteruje sie po tablicy F, z kazda iteracja
dodaje do kolejnki piorytetowej ilosc paliwa na danej stacji, jesli suma paliwa jest zerem to znaczy ze powinienem,
wczesniej zatankowac na taj stacji na ktorej bylo najwiecej paliwo, wiec zwiekszam wynik o 1 i tez w kazdej iteracji
zmniejszam sume paliwa o 1(koszt przejscia miedzy dwiema sasiednimi komorkami)
Zlozonosc DFS O(nm), iteracji po tablicy F O(mlogm), sumarycznie O(nm + mlogm)
'''
from zad8testy import runtests
import heapq

def count_fuel(x,y, T, Vis):
    n = len(T)
    m = len(T[0])
    Q = []
    sum_fuel = 0
    Q.append([x,y])
    Vis[x][y] = 1
    while Q:
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
    print(F)
    Q = []
    actual_fuel = 0
    for i in range(m-1):
        if F[i]:
            heapq.heappush(Q,-F[i])
        if actual_fuel == 0:
            res +=1
            max_station = heapq.heappop(Q)
            actual_fuel-=max_station
        actual_fuel -= 1

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

