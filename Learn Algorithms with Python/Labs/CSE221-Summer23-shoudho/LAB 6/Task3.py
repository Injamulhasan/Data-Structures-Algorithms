import heapq

def r_inp(f3):

    f = open(f3, "r")
    a,b = map(int, f.readline().split())
    gr = [[] for _ in range(a+ 1)]
    for i in range(b):
        x,y,z= map(int, f.readline().split())
        gr[x].append((y,z))
        gr[y].append((x,z))
    f.close()
    return a, gr

def dijkstra(gr,a):

    dis= [float('inf')] * (a+ 1)
    dis[1] = 0
    mn= [(1, 0)]
    
    while mn:
        x, max_weight = heapq.heappop(mn)
        if x == a:
            return max_weight
        if max_weight > dis[x]:
            continue
        for y,z in gr[x]:
            if max(max_weight,z) < dis[y]:
                dis[y] = max(max_weight,z)
                heapq.heappush(mn, (y, dis[y]))
    return -1

def w_out(out, f3):

    f = open(f3, "w")
    if out == -1:
        f.write("Impossible")
    else:
        f.write(str(out))
    f.close()

f3 = "input3.txt"
a, gr= r_inp(f3)
res= dijkstra(gr, a)
w_out(res, "output3.txt")
