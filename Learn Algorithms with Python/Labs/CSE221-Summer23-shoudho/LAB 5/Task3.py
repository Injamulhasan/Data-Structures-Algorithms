def dfs_stack(gr, vt, visit, st):
    visit[vt] = True
    for neigh in gr[vt]:
        if not visit[neigh]:
            dfs_stack(gr, neigh, visit, st)
    st.append(vt)

def fill_stack(gr, n):
    st = []
    visit = [False] * (n + 1)
    for vt in range(1, n + 1):
        if not visit[vt]:
            dfs_stack(gr, vt, visit, st)
    return st

def dfs_scc(gr, vt, visit, scc):
    visit[vt] = True
    scc.append(vt)
    for neigh in gr[vt]:
        if not visit[neigh]:
            dfs_scc(gr, neigh, visit, scc)

def find_scc(gr, n, st):
    scc_list = []
    visit = [False] * (n + 1)
    while st:
        vt = st.pop()
        if not visit[vt]:
            scc = []
            dfs_scc(gr, vt, visit, scc)
            scc_list.append(scc)
    return scc_list

def r_inp(f3):
    f = open(f3, 'r')
    x, y = map(int, f.readline().split())  
    graph = {i: [] for i in range(1, x + 1)}
    for i in range(y):
        line = f.readline().split()
        u = int(line[0])
        v = int(line[1])
        graph[u].append(v)
    f.close()
    return x, y, graph

def w_out(f, scc_components):  
    f = open(f, 'w')  
    for scc in scc_components:
        res = []
        for i in scc:
            res.append(str(i))
        f.write(" ".join(res) + "\n")
    f.close()

f3 = "input3.txt"
x, y, gr = r_inp(f3)
stack = fill_stack(gr, x)
rev_gr = {i: [] for i in range(1, x + 1)}

for vt in gr:
    for neigh in gr[vt]:
        rev_gr[neigh].append(vt)

scc_components = find_scc(rev_gr, x, stack)
w_out("output3.txt", scc_components)
