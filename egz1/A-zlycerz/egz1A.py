'''
Lukasz Kluza
Moj pomysl opiera sie na tym aby rozwazyc kazdy mozliwy zamek jako ten ktory zostanie obrabowyany,
kolejno pozniej szukam najkrotszej drogi do tego zamku od startu(Djikstra na orginalnym grafie)
i od potencjalnego zamku do zamku koncowego(Djikstra na grafie gdzie wagi grawedzi sa pomnoszone przez 2 i dodane r)
kolejno pozniej wybieram minimum z kosztu z 's' do zamku obrabowanego + z tego zamku to zamku 't' - wartosc lupu
Zlozonosc: djikstra O(ElogV) = O(V^2logV), djikstre wykoniuje po dwa razy dla kazdego wierzcholka czyli,
O(2V^3logV) = O(V^3logV)
'''


from egz1Atesty import runtests
import heapq
from math import inf


def Djikstra(G, v, w):
    if v == w:
      return 0
    n = len(G)
    dist = [inf]*n
    Q = []
    heapq.heappush(Q, (0, v))
    dist[v] = 0
    while Q:
        cost, v = heapq.heappop(Q)
        for k in G[v]:
            if dist[k[0]] > dist[v] + k[1]:
                heapq.heappush(Q, (k[1], k[0]))
                dist[k[0]] = dist[v] + k[1]
    return dist[w]


def gold(G,V,s,t,r):
    res = inf
    n = len(G)
    G2 = [[] for _ in range(n)]
    for v in range(n):
        for x, cost in G[v]:
            G2[v].append([x, 2*cost+r])
    for i in range(n):
        temp = Djikstra(G, s, i) - V[i] + Djikstra(G2, i, t)
        res = min(res, temp)
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
