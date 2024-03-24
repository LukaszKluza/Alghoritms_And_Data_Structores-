# Lukasz Kluza
# Daną liste wierzcholkow, ktore leza w osobliwosci lacze w cykl,
# poniewaz dla wiercholkow lezaczych w osobliwosci nie ma znaczenia
# czy wybierzemy droge pezposrednia czy posrednia, sumaryczny koszt i tak wyniesie 0
# kolejno na utworzonym grafie puszczam algorytm Djikstry
# Zlozonosc: O(ElogV)
from zad5testy import runtests
from math import inf
import heapq

def Djikstra(G, v, dist):
    Q = []
    heapq.heappush(Q, (0, v))
    dist[v] = 0
    while Q:
        cost, v = heapq.heappop(Q)
        for k in G[v]:
            if dist[k[0]] > dist[v] + k[1]:
                heapq.heappush(Q, (k[1], k[0]))
                dist[k[0]] = dist[v]+k[1]

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n)]
    if len(S) > 0:
        first = last = S[0]
    for i in range(1, len(S)):
        v = S[i]
        G[last].append((v, 0))
        G[v].append((last, 0))
        last = v
    G[first].append((v, 0))
    G[v].append((first, 0))
    for x in E:
        v = x[0]
        w = x[1]
        cost = x[2]
        if len(G[v]) >= 2 and G[v][0][0] != w and G[v][1][0] != w:
            G[v].append((w, cost))
            G[w].append((v, cost))
        elif len(G[v]) < 2:
            G[v].append((w, cost))
            G[w].append((v, cost))
    d = [inf]*n
    Djikstra(G, a, d)
    if d[b] == inf:
        return None
    return d[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )