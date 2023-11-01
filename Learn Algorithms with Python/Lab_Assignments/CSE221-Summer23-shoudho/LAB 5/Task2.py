from collections import defaultdict, deque

def sq(a, pre):
    gr = defaultdict(list)
    in_deg= [0]*(a+1)

    for x,y in pre:
        gr[x].append(y)
        in_deg[y]+=1
    que = deque()
     
    for i in range(1, a+1):
        if in_deg[i]==0:
            que.append(i)
    
    l1 = []
    while que and len(l1) <a:
        que = deque(sorted(que))
        cour = que.popleft()
        l1.append(cour)
        for i in gr[cour]:
            in_deg[i]-=1
            if in_deg[i]==0:  
                que.append(i)
    if len(l1) == a:
        return l1
    else:
        return "IMPOSSIBLE"

def r_inp(f2):
    f = open(f2,'r')
    I, J = map(int, f.readline().split())
    l2 = []
    for i in range(J):
        line = f.readline().split()
        l2.append((int(line[0]), int(line[1])))
    f.close()
    return I,l2

def w_out(f2,s):
    f = open(f2,'w')
    if s== "IMPOSSIBLE":
        f.write(s)
    else:
        l3 = []
        for i in s:
            l3.append(str(i))
        f.write(" ".join(l3))
    f.close()

f2 = "input2.txt"
I, pre = r_inp(f2)
s = sq(I, pre)
w_out("output2.txt", s)
