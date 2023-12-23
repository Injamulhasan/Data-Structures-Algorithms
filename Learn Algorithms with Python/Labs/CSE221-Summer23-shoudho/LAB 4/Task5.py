#5
f5 = open('input5.txt', 'r')
f6 = open('output5.txt', 'w')

a, b, d = map(int, f5.readline().split())
adj_list = [[] for _ in range(a+1)]

for _ in range(b):
    x, y = map(int, f5.readline().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

que = [(1, [1])]
visit = [False]*(a+1)
l1 = []

while que:
    node, path = que.pop(0)
    if d == node:
        l1 = path
        break
    
    visit[node] = True
    for neigh in adj_list[node]:
        if not visit[neigh]:
            que.append((neigh, path +[neigh]))

str_p = [str(i) for i in l1]
t = len(str_p) - 1


f6.write(f'Time: {t}\nShortest Path: {" ".join(str_p)}')

f5.close()
f6.close()
