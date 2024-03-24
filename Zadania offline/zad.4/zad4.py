from zad4testy import runtests

def longer( G, s, t ):
    n = len(G)
    vis = [0] * n
    par = [0] * n
    Q = []
    Q.append(s)
    vis[s] = 1
    par[s] = None
    dis = [0] * n
    # print(n)
    while len(Q) > 0:
        v = Q.pop(0)
        # print(v)
        for x in G[v]:
            if vis[x] == 0:
                par[x] = v;
                Q.append(x)
                vis[x] = 1
                dis[x] = dis[v] + 1
    # print(par)
    min_dist = dis[t]
    #print("MIN  ", min_dist)
    path = [0] * n
    k = t
    while k != None:
        path[k] = 1
        k = par[k]
    #print("P ", path)
    # print(dis)
    Q.append(s)
    Q0 = []
    Q1 = []
    Q1.append(s)
    # print("\n\n")
    vis[s] = -1
    last_v = s
    flag = 1
    while len(Q1) + len(Q0) > 0:
        if len(Q0) > 0:
            v = Q0.pop(0)
        else:
            v = Q1.pop(0)
        #print(v, "Q0: ", Q0, "   Q1:  ", Q1)
        if path[v] == 1:
            last_v = v
            flag = 1
        for x in G[v]:
            #print(" ", x, path[x])
            if vis[x] != -1:
                vis[x] = -1
                if path[x] == 1:
                    Q1.append(x)
                else:
                    Q0.append(x)
            if path[x] == 1 and x != v and path[v] != 1 and last_v != x and flag == 1 and par[v]!=x:
                print("OK", x, "Dx: ", dis[x], v, ", Dv: ", dis[v])
                if dis[x] <= dis[v]:
                    #print("Tak", x, v)
                    for x in G[last_v]:
                        if path[x] == 1:
                            #print("KOK")
                            return min(x, last_v), max(x, last_v)
                else:
                    flag = 0
    # print("NIE")
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )