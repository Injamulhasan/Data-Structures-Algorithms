#3
f3 = open('input3.txt', 'r')
f4 = open('output3.txt', 'w')

a,b = map(int, f3.readline().split())
adj_list = [[] for _ in range(a+1)]

for _ in range(b):
    x,y = map(int, f3.readline().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

stack = [1]
visit = [False]*(a+1)
path = []

while stack:
    x = stack.pop()
    if not visit[x]:
        path.append(x)
    visit[x] = True
    for neigh in adj_list[x]:
        if not visit[neigh]:
            stack.append(neigh)

str_p = []
for i in path:
    str_p.append(str(i))


f4.write(" ".join(str_p))

f3.close()
f4.close()
