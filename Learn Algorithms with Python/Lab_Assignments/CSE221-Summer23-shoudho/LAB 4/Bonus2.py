
from collections import defaultdict

def Dfs(nd, g, gr, visit):
    visit[nd] = True
    c = 1 if g[nd] == 'Vampire' else 0
    for neigh in gr[nd]:
        if not visit[neigh]:
            c += Dfs(neigh, g, gr, visit)
    return c

def solve_case(case_n, n, fights):

    gr = defaultdict(list)
    for x, y in fights:
        gr[x].append(y)
        gr[y].append(x)

    g = defaultdict(lambda: 'Unknown')
    visit = defaultdict(bool)

    for nd in gr:
        if not visit[nd]:
            stack = [nd]
            g[nd] = 'Vampire'
            visit[nd] = True
            while stack:
                cur = stack.pop()
                for neigh in gr[cur]:
                    if not visit[neigh]:
                        visit[neigh] = True
                        g[neigh] = 'Lykan' if g[cur] == 'Vampire' else 'Vampire'
                        stack.append(neigh)

    vamp_c = Dfs(1, g, gr, defaultdict(bool))
    lykan_c = n - vamp_c

    with open('b2out.txt', 'w') as f3:
        f3.write("Case {}: {}\n".format(case_n, max(vamp_c, lykan_c)))

f2 = open('b2in.txt', 'r')
t = int(f2.readline())

for i in range(t):
    T = int(f2.readline())

    fights = []
    for j in range(T):
        x,y = map(int, f2.readline().split())
        fights.append((x,y))

    solve_case(i+1,T,fights)

f2.close()


