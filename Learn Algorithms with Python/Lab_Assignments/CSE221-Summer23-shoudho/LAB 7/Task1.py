def r_inp(f1):

    f = open(f1, 'r')
    T = int(f.readline())
    m= []
    for i in range(T):
        a,b = map(int, f.readline().split())
        m.append([a,b])
    f.close()
    return T, m

def w_out(out, f1):

    f = open(f1, 'w')
    f.write(str(len(out)) + "\n")
    for i in out:
        a = i[0]
        b = i[1]
        f.write(f'{a} {b}\n')
    f.close()

f1 = "input1.txt"
T,m = r_inp(f1)
list1 = []
c = 0
list1.append(m[0])
m.sort(key=lambda a: a[1])

for i in range(1, T):
    if m[c][1] <= m[i][0]:
        c = i
        list1.append(m[i])

f1 = "output1.txt"
w_out(list1, f1)

