def longer(G,s,t):
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
     #print(par)
     min_dist = dis[t]
     print("MIN  ", min_dist)
     path = [0] * n
     k = t
     while k != None:
         path[k] = 1
         k = par[k]
     print("P ",path)
     # print(dis)
     Q.append(s)
     # print("\n\n")
     vis[s] = -1
     last_v = s
     while len(Q) > 0:
         v = Q.pop(0)
         print(v,Q)
         if path[v] == 1:
             last_v == v
         for x in G[v]:
             print(" ",x, path[x])
             if vis[x] != -1:
                 vis[x] = -1
                 if path[x] == 1:
                     Q.append(x)
                 else:
                     Q.insert(0, x)
             if path[x] == 1 and x != v and path[v] != 1 and last_v!=x:
                 print("OK",x,"Dx: ",dis[x],v,", Dv: ",dis[v])
                 if dis[x] < dis[v]:
                     print("Tak", x,v)
                     for x in G[last_v]:
                         if path[x] == 1:
                             print("KOK")
                             return min(x, last_v), max(x, last_v)
                 else:
                     return None
     # print("NIE")
     return None

G1 = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
s = 0
t = 2
G3 = [[],[2,5],[1,3],[2,4],[3,6],[1,6,7],[4,5,7],[5,6]]
G4 = [[3, 67, 75, 11, 92, 83, 19, 31, 63], [2, 38, 6, 42, 78, 30, 86, 54, 90, 62], [97, 1, 33, 65, 5, 9, 73, 13, 47, 81, 49, 29, 17, 85, 53, 93], [0, 36, 8, 44, 16, 48, 80, 52, 84, 88, 24, 56, 92], [97, 99, 35, 67, 39, 71, 27, 43, 75, 76, 47, 79, 83, 51, 55, 87, 59, 95], [2, 34, 90, 38, 6, 70, 14, 78, 46, 18, 86, 26, 94], [97, 1, 69, 5, 73, 9, 45, 81, 17, 49, 85, 93], [16, 20, 24, 29, 32, 36, 44, 48, 52, 56, 63, 64, 67, 68, 72, 76, 80, 84, 96], [3, 67, 99, 39, 75, 43, 79, 15, 51, 55, 27, 31, 95, 63], [2, 6, 10, 18, 22, 30, 34, 38, 42, 50, 54, 58, 62, 66, 78, 82, 86, 90, 98], [37, 69, 9, 77, 81, 85, 21, 57], [0, 64, 32, 68, 36, 40, 76, 28, 48, 80, 16, 20, 52, 24, 60], [99, 35, 68, 27, 75, 15, 50, 51, 59, 63], [34, 66, 2, 98, 70, 38, 42, 78, 14, 18, 50, 30, 82, 22, 54, 86, 58, 94], [89, 97, 69, 5, 41, 45, 77, 13, 17, 81, 93, 53, 21, 85, 25, 61], [64, 32, 96, 36, 72, 8, 12, 76, 80, 48, 52, 24, 56, 88], [35, 3, 7, 39, 71, 43, 75, 11, 79, 51, 83, 19, 27, 31, 95], [2, 34, 6, 70, 38, 74, 78, 14, 18, 22, 54, 62, 90, 94], [96, 33, 69, 5, 37, 9, 45, 13, 81, 29, 49, 93, 85, 53, 17, 57, 61, 25], [96, 64, 0, 68, 36, 40, 44, 92, 48, 16, 80, 20, 84, 24, 88, 28], [35, 71, 7, 59, 27, 11, 75, 78, 79, 47, 19, 51, 58, 91, 31, 63, 95], [98, 34, 90, 42, 10, 14, 82, 22, 62, 26, 94], [97, 33, 65, 37, 9, 77, 13, 45, 17, 49, 81, 61, 85, 21, 25, 93, 57], [96, 64, 68, 36, 40, 44, 84, 52, 88, 60], [35, 3, 99, 71, 7, 39, 11, 43, 15, 47, 79, 19, 83, 87, 91, 95], [66, 26, 98, 58, 38, 99, 74, 78, 14, 46, 50, 18, 22, 86, 54, 90, 62], [33, 65, 5, 37, 41, 45, 77, 49, 93, 85, 53, 21, 25, 29], [64, 36, 68, 4, 8, 12, 44, 16, 48, 84, 52, 20, 88, 60], [71, 43, 11, 47, 79, 19, 83, 87, 91, 95], [34, 2, 26, 90, 38, 7, 74, 42, 78, 46, 50, 18, 82, 54, 30, 58, 61, 94], [97, 1, 37, 9, 73, 41, 77, 13, 81, 29, 61, 53, 57, 93], [64, 0, 68, 69, 8, 80, 16, 20, 56, 92], [34, 99, 67, 69, 7, 39, 11, 43, 15, 79, 83, 87, 57, 91, 63, 95], [2, 34, 98, 38, 70, 42, 78, 46, 82, 50, 18, 22, 26, 94], [32, 33, 97, 5, 37, 41, 9, 13, 17, 93, 21, 53, 85, 89, 29, 62], [96, 64, 36, 4, 40, 12, 16, 48, 20, 84, 24, 92], [3, 35, 67, 39, 27, 59, 7, 11, 43, 15, 47, 79, 51, 19, 23, 91, 95], [98, 66, 34, 10, 42, 18, 50, 54, 22, 62, 94, 26, 30], [33, 97, 1, 5, 69, 9, 45, 13, 81, 17, 49, 61, 85, 89, 29, 25], [64, 32, 68, 36, 4, 8, 44, 92, 80, 16, 52, 56, 24, 60], [99, 67, 35, 75, 11, 43, 47, 79, 19, 23, 55, 87, 91, 95, 63], [34, 66, 26, 42, 14, 46, 78, 82, 50, 30, 94, 58, 62], [1, 97, 33, 69, 37, 9, 41, 13, 45, 77, 81, 29, 53, 85, 21, 89, 93], [64, 96, 32, 4, 36, 8, 40, 44, 28, 16, 80, 24, 56, 92], [3, 67, 39, 7, 71, 43, 47, 79, 19, 87, 23, 27, 63], [26, 70, 38, 6, 42, 74, 14, 78, 50, 18, 22, 86, 58, 62], [33, 69, 5, 41, 73, 81, 29, 61, 89, 93, 25, 57], [96, 2, 4, 36, 40, 44, 28, 76, 48, 84, 20, 56, 24, 88, 60, 57], [35, 3, 7, 71, 27, 11, 15, 47, 79, 83, 19, 51, 55, 91, 63], [2, 90, 70, 6, 38, 74, 18, 54, 22, 26], [65, 33, 37, 69, 9, 41, 12, 45, 13, 53, 56, 25, 29, 57], [64, 97, 68, 4, 36, 72, 8, 12, 16, 48, 81, 84, 52, 20, 92], [3, 99, 39, 27, 7, 71, 75, 11, 15, 51, 83, 23, 87, 91, 95], [2, 66, 34, 90, 70, 42, 14, 78, 82, 50, 18, 62, 94, 26, 30], [1, 97, 37, 69, 73, 9, 13, 77, 81, 49, 17, 85, 25, 29], [68, 4, 40, 8, 76, 92, 48, 88, 60], [96, 67, 3, 39, 7, 59, 43, 75, 47, 79, 15, 50, 83, 87, 58, 91, 31, 95], [32, 66, 90, 10, 46, 78, 47, 18, 82, 50, 30, 22, 86, 62, 58, 94], [69, 41, 73, 9, 45, 13, 61, 93, 85, 20, 56, 57, 29, 25, 63], [36, 68, 4, 12, 76, 92, 84, 20, 56, 60], [99, 39, 71, 59, 75, 11, 47, 79, 23, 87, 55, 27, 63, 95], [70, 38, 74, 78, 14, 46, 18, 82, 22, 30, 94, 58, 29, 62], [1, 34, 69, 37, 73, 41, 9, 45, 77, 17, 21, 53, 57, 61, 25], [0, 64, 32, 68, 7, 8, 40, 72, 76, 44, 12, 92, 48, 20, 84, 88, 58, 60], [99, 35, 7, 39, 11, 43, 75, 15, 51, 19, 23, 27, 63, 31], [66, 2, 74, 78, 50, 82, 86, 22, 26], [89, 65, 37, 41, 73, 9, 13, 77, 81, 53, 57, 93, 25], [32, 0, 4, 68, 36, 7, 8, 40, 76, 44, 80, 56, 88], [99, 67, 39, 7, 59, 27, 11, 75, 12, 79, 51, 19, 23, 55, 91, 31, 63, 95], [32, 6, 38, 70, 42, 74, 10, 46, 14, 18, 50, 54, 58, 62, 31], [97, 33, 69, 5, 13, 45, 77, 49, 17, 85, 53, 89, 61], [96, 4, 76, 44, 28, 48, 16, 80, 84, 20, 52, 24, 60], [99, 7, 75, 15, 79, 83, 51, 95, 63], [98, 66, 2, 6, 74, 46, 82, 54, 30, 86, 94, 58, 62], [65, 97, 69, 73, 77, 45, 49, 29, 17, 61, 89, 93, 25], [64, 0, 68, 4, 72, 8, 40, 12, 76, 92, 80, 16, 52, 84, 20, 56, 60], [67, 4, 71, 7, 91, 75, 11, 79, 47, 15, 83, 87, 55, 59, 63], [98, 66, 70, 42, 10, 74, 14, 78, 82, 30, 54, 22, 62, 26, 94], [1, 5, 9, 13, 17, 20, 25, 29, 33, 41, 45, 53, 57, 61, 65, 77, 81, 85, 89, 93, 99], [4, 8, 16, 20, 24, 28, 32, 36, 40, 44, 48, 56, 60, 68, 72, 76, 80, 92, 96], [67, 3, 39, 7, 71, 75, 11, 43, 15, 79, 19, 83, 87, 31], [66, 2, 6, 38, 42, 10, 78, 14, 46, 18, 51, 54, 22, 87, 90, 30], [33, 65, 73, 9, 41, 77, 13, 29, 21, 53, 57, 61], [32, 0, 4, 72, 76, 28, 48, 16, 80, 52, 84, 88, 24, 56, 92], [99, 35, 3, 7, 71, 59, 91, 75, 47, 51, 19, 83, 23, 27, 63, 95], [2, 34, 58, 90, 70, 38, 6, 98, 42, 10, 14, 78, 18, 22, 54, 26, 94], [65, 1, 5, 73, 9, 13, 45, 89, 93, 25, 57], [32, 4, 40, 44, 76, 60, 28, 80, 81, 52, 56, 24, 88, 92], [3, 67, 91, 15, 47, 83, 19, 55, 87, 23, 27, 63], [98, 66, 34, 38, 70, 74, 42, 78, 46, 14, 86, 94], [1, 5, 9, 81, 49, 29, 17, 53, 85, 21, 25, 93, 57], [32, 68, 36, 40, 76, 92, 48, 20, 52, 84, 56, 24, 88, 28], [0, 35, 3, 39, 91, 75, 43, 79, 19, 83, 55, 51, 87, 59, 63, 95, 31], [98, 2, 34, 58, 66, 26, 6, 74, 42, 46, 78, 14, 18, 22, 86, 94, 90, 30], [89, 33, 5, 37, 73, 41, 77, 13, 17, 61, 93, 21, 85, 53, 57, 29], [96, 32, 36, 68, 4, 72, 40, 8, 60, 92, 16, 20, 84, 52, 24, 56, 28], [35, 99, 71, 7, 43, 15, 47, 79, 18, 19, 23, 56, 95], [98, 2, 34, 4, 6, 38, 70, 42, 74, 14, 51, 22, 54, 30], [97, 33, 37, 73, 9, 77, 13, 21, 85, 89, 93, 25], [32, 64, 96, 4, 68, 40, 72, 8, 12, 78, 84, 52, 24, 25, 60]]
G5 = [[1,4],[0,2,7],[1,3,6,7],[2],[0,5],[4,6],[5,2],[1,2]] 
G6 = [[1,4,7],[0,2],[1,3,6,7],[2],[0,5],[4,6],[5,2],[0,2]]
print(longer(G6,0,3))
#print(longer(G1,s,t))

###########################################