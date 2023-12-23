def r_inp(f):
    f1= open(f, 'r')
    a,b = map(int, f1.readline().split())
    pre = [tuple(map(int, f1.readline().split())) for _ in range(b)]
    f1.close() 
    return a, pre

def bfs_order(a, pre):
    gr= {i: [] for i in range(1,a + 1)}
    in_deg = {i: 0 for i in range(1,a + 1)}
    for A, B in pre:
        gr[A].append(B)
        in_deg[B] += 1

    que = []
    res= []

    for i in range(1,a + 1):
        if in_deg[i] == 0:
            que.append(i)

    while que:
        c = que.pop(0)
        res.append(c)
        for i in gr[c]:
            in_deg[i] -= 1
            if in_deg[i] == 0:
                que.append(i)

    return res if len(res) == a else None

def w_out(output, f):
    f2 = open(f, "w")
    f2.write("BFS Order--")
    if output:
        for c in output:
            f2.write(" " + str(c))
    else:
        f2.write(" IMPOSSIBLE")
    f2.close()

f = "input1a.txt"
a,pre = r_inp(f)
order_bfs = bfs_order(a, pre)
w_out(order_bfs, "output1a.txt")
