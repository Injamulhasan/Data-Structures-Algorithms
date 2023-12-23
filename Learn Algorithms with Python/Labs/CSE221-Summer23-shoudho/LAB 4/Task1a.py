#1a
f = open('input1a.txt', 'r')
f2 = open('output1a.txt', 'w')

T = f.readlines()
a, b = T[0].split()
a = int(a)
b = int(b)

adj_matr = [[0]*(a+1) for _ in range(a+1)]

for i in range(1,b+1):
    x, y, z = T[i].split()
    x = int(x)
    y = int(y)
    z = int(z)
    adj_matr[x][y] = z

for r in adj_matr:
    r_str = ""
    for i in range(len(r)):
        r_str += str(r[i]) + " "
    f2.write(r_str.strip() + "\n")

f.close()
f2.close()
