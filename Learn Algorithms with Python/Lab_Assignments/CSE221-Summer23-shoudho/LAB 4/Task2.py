#2
f2 = open('input2.txt', 'r')
f3 = open('output2.txt', 'w')

a,b = map(int, f2.readline().split())
adj_list = [[] for _ in range(a+1)]

for _ in range(b):
    x,y = map(int, f2.readline().split())
    adj_list[x].append(y)
    adj_list[y].append(x)


que = [1]
visit = [False]*(a+1)
path = []

while que:
    x = que.pop(0)
    path.append(x)
    visit[x] = True
    for neigh in adj_list[x]:
        if not visit[neigh]:
            que.append(neigh)

str_p = []
for i in path:
    str_p.append(str(i))


f3.write(" ".join(str_p))

f2.close()
f3.close()
