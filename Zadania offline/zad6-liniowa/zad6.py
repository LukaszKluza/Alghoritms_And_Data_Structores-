#Lukasz Kluza
#Algorytm szuka największego skojarzenia w grafie dwudzielnym
#Czyli takiego maksymalnego przeplywu aby jeden pracownik obslugiwal tylko jedna maszyne
#Zlozonosc algorytmu to O(n^3)

from zad6testy import runtests


def DFS(G, s, b):
    n = len(G)
    parent = [[None, None]]*n
    vis = [0]*n
    vis[s] = 1
    Q = [s]
    while Q:
        v = Q.pop()
        if v == b:
            break
        for w, active, nr in G[v]:
            if active > 0 and vis[w] == 0:
                Q.append(w)
                vis[w] = 1
                parent[w] = [v, G[w][nr][2]]
    if vis[b] == 0:
        return None
    t = [b, None]
    while parent[t[0]][0] is not None:
        w = t[0]
        v = parent[t[0]][0]
        idx_1 = parent[t[0]][1]
        idx_2 = G[v][idx_1][2]
        G[v][idx_1][1] = 0
        G[w][idx_2][1] = 1
        t = parent[t[0]]
    return True


def binworker(M):
    n = len(M)
    G = [[] for _ in range(2*n+2)]
    for i in range(n):
        for v in M[i]:
            G[i+n].append([v, 1, len(G[v])])
            G[v].append([i+n, 0, len(G[i+n])-1])

    for i in range(n):
        G[i].append([2*n+1, 1, len(G[2*n+1])])
        G[2*n+1].append([i, 0, len(G[i])-1])
        G[i+n].append([2 * n, 0, len(G[2 * n])])
        G[2 * n].append([i+n, 1, len(G[i+n]) - 1])

    path = DFS(G, 2*n, 2*n+1)
    flow = 0
    while path:
        flow += 1
        path = DFS(G, 2*n, 2*n+1)
    return flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
