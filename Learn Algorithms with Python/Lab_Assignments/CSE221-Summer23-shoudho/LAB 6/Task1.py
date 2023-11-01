import heapq

def r_inp(f1):

    f = open(f1, "r")
    a,b = map(int, f.readline().split())
    gr = [[] for _ in range(a+1)]
    for _ in range(b):
        x,y,z = map(int, f.readline().split())
        gr[x].append((y,z))
    T= int(f.readline())
    f.close()
    return a, gr,T

def w_out(out, f1):

    f = open(f1, "w")
    for val in out:
        f.write(str(val) + " ")
    f.close()

f1 = "input1.txt"
a, gr,T = r_inp(f1)
dis = [float('inf')] * (a+ 1)
dis[T] = 0
mn = [(0, T)]

while mn:
    
    d,x = heapq.heappop(mn)
    if d > dis[x]:
        continue
    for y,z in gr[x]:
        if dis[x] +z < dis[y]:
            dis[y] = dis[x] +z
            heapq.heappush(mn, (dis[y],y))

out = [str(dis[i]) if dis[i] != float('inf') else "-1" for i in range(1, a+ 1)]
w_out(out, "output1.txt")
