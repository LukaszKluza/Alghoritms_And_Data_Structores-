# Łukasz Kluza
# Algortym polega na znalezieniu wszystkich najkrótszych możliwych ścieżek z 's' do 't'
# W tym celu wykonuje dwa razy algorytm BFS, raz z 's' a raz z 't'
# Kolejno z krawędzi które należą do zbioru najkrótszych ścieżek robię graaf, w którym wyszukuję most
# Jeśli on istnieje to wystarczy go usunąć i w tedy rozpójnie najkrótszą ścieżkę
# co jest równoznaczne z rozwiązaniem zadania
from zad4testy import runtests
from collections import deque
from math import inf


def BFS(G, v, dist):
    Q = deque()
    Q.append(v)
    dist[v] = 0
    while len(Q) > 0:
        v = Q.popleft()
        for x in G[v]:
            if dist[x] == -1:
                dist[x] = dist[v]+1
                Q.append(x)


def DFS(G, v, d, par, low):
    time = 0

    def DFS_Visit(G, v, d, par, low):
        nonlocal time
        time += 1
        d[v] = time
        low[v] = time
        for x in G[v]:
            if d[x] != -1:
                if x != par[v]:
                    low[v] = min(low[v], d[x])
            else:
                par[x] = v
                DFS_Visit(G, x, d, par, low)
                low[v] = min(low[x], low[v])


    DFS_Visit(G, v, d, par, low)


def longer( G, s, t ):
    n = len(G)
    dist1 = [-1]*n
    dist2 = [-1]*n
    par = [0] * n
    low = [inf]*n
    vis = [0]*n
    d = [-1]*n
    BFS(G, s, dist1)
    if dist1 == -1:
        return None
    BFS(G, t, dist2)
    min_len = dist1[t]
    path = [[] for _ in range(n)]
    Q = deque()
    Q.append(s)
    vis[s] = 1
    while Q:
        v = Q.popleft()
        for x in G[v]:
            if dist1[x] + dist2[x] == min_len:
                path[v].append(x)
                if vis[x] == 0:
                    vis[x] = 1
                    Q.append(x)
    DFS(path, s, d, par, low)
    par[0] = -1
    for i in range(n):
        if d[i] == low[i] and par[i] != -1:
            return par[i], i
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
