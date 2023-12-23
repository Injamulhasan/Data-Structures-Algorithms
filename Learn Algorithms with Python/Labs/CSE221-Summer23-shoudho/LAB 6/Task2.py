import heapq

def dijkstra(st, adj,a):

    dis = [float('inf')] * (a+ 1)
    dis[st] = 0
    hp = [(0, st)]
    while hp:
        d,x = heapq.heappop(hp)
        for y,z in adj[x]:
            if dis[x] + z < dis[y]:
                dis[y] = dis[x] + z
                heapq.heappush(hp, (dis[y],y))
    return dis

def r_inp(f2):

    f = open(f2, "r")
    a,b = map(int, f.readline().split())
    adj = [[] for _ in range(a+ 1)]

    for _ in range(b):
        x,y,z= map(int, f.readline().split())
        adj[x].append((y,z))

    m,n= map(int, f.readline().split())
    f.close()
    return a, adj,m,n

def w_out(out, f2):

    f = open(f2, "w")
    if out[0] == -1:
        f.write("Impossible")
    else:
        f.write(f'Time: {out[0]}\nNode: {out[1]}')
    f.close()

f2 = "input2.txt"
a, adj,m,n = r_inp(f2)
dis_s = dijkstra(m, adj,a)
dis_t = dijkstra(n, adj,a)
meet_n = -1
min_t = float('inf')

for n in range(a+ 1):
    
    if min_t > max(dis_s[n], dis_t[n]):
        min_t= max(dis_s[n], dis_t[n])
        meet_n = n

out = (min_t, meet_n)
w_out(out, "output2.txt")
