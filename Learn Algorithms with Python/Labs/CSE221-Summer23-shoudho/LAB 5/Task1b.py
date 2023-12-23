def dfs(c, gr, visit, st):
    visit[c] = True
    for i in gr[c]:
        if not visit[i]:
            dfs(i, gr, visit, st)
    st.append(c)

def dfs_ord(N, pre):
    gr= {i: [] for i in range(1, N+1)}
    for A, B in pre:
        gr[A].append(B)
    visit= [False] * (N+1)
    st = []

    for i in range(1, N+1):
        if not visit[i]:
            dfs(i, gr, visit, st)

    return st[::-1] if len(st) == N else None

def r_inp(f):
    f1 = open(f, 'r')
    x,y = map(int, f1.readline().split())
    pre = []
    for i in range(y):
        line = f1.readline().split()
        pre.append((int(line[0]), int(line[1])))
    f1.close()
    return x, pre

def w_out(f, order):
    f1 = open(f, 'w')
    if order:
        f1.write("DFS Order--")
        for course in order:
            f1.write(" " + str(course))
    else:
        f1.write("IMPOSSIBLE")
    f1.close()

f1 = "input1b.txt"
x, pre = r_inp(f1)
ord_dfs = dfs_ord(x, pre)
w_out("output1b.txt", ord_dfs)






