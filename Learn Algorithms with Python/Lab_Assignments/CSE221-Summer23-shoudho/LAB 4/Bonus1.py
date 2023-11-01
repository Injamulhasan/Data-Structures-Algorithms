#b1
c=0
l1 = []
f2 = open("b1in.txt", "r")
c = int(f2.readline())
for i in range(c-1):
    x,y = map(int,f2.readline().split())
    l1.append((x,y))

farthest = (1,2)
max_dis = 0

for x in range(1, c+1):

    for y in range(x+1, c+1):
        if (x,y) not in l1 and (y,x) not in l1:
            visit= [False]*(c+1)
            dis = 0
            current=x

            while current!=y:
                visit[current] = True
                dis += 1

                for neigh in range(1, c+1):
                    if (current, neigh) in l1 or (neigh,current) in l1:
                        if not visit[neigh]:
                            current= neigh
                            break
                else:
                    break
            else:
                if dis>max_dis:
                    max_dis = dis
                    farthest= (x,y)

f3 = open("b1out.txt", "w")
f3.write(f"{farthest[0]} {farthest[1]}\n")
f2.close()
f3.close()
