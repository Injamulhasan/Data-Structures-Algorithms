f6 = open('input6.txt', 'r')

a,b = map(int, f6.readline().split())
l1 = []

for _ in range(a):
    T = f6.readline().strip()
    l1.append(T)

f6.close()

def Dfs(visit,l1, i, j):

    global a,b
    stack = [(i, j)]
    c= 0

    while stack:
        r,col = stack.pop()
        if r < 0 or col < 0 or r>= a or col >=b:
            continue
        if l1[r][col] == "#" or visit[r][col]:
            continue
        visit[r][col] = True
        if l1[r][col] == "D":
            c+= 1
        stack.append((r+1,col))
        stack.append((r-1,col))
        stack.append((r,col-1))
        stack.append((r,col+1))

    return c

max_diam = 0

for i in range(a):
    for j in range(b):
        if l1[i][j] != "#":
            visit = [[False for _ in range(b)] for _ in range(a)]
            diam = Dfs(visit,l1, i, j)
            max_diam = max(diam, max_diam)

with open('output6.txt', 'w') as f:
    f.write(str(max_diam))


