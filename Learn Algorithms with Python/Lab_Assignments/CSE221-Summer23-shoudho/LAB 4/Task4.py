
f4 = open('input4.txt', 'r')

a,b= map(int, f4.readline().split())
adj_list = [[] for _ in range(a+1)]

for _ in range(b):
    x,y = map(int, f4.readline().split())
    adj_list[x].append(y)

stack = [(1, [1])]
cycle = False

while stack:
    node, path = stack.pop()
    for neigh in adj_list[node]:
        if neigh in path:
            cycle = True
        else:
            stack.append((neigh, path+[neigh]))
    if cycle:
        break

if cycle:
    print('YES', file=open('output4.txt', 'w'))
else:
    print('NO', file=open('output4.txt', 'w'))

f4.close()
