#1b
f2 = open('input1b.txt', 'r')
f3 = open('output1b.txt', 'w')

T = f2.readlines()
a,b = T[0].split()
a = int(a)
b = int(b)

adj_list=[[] for _ in range(a+1)]

for i in range(1,b+1):
    x, y, z = T[i].split()
    x = int(x)
    y = int(y)
    z = int(z)
    adj_list[x].append((y,z))

for i in range(a):
    r_str = f"{i}: "
    for y,z in adj_list[i]:
        r_str += f"({y}, {z}), "
    r_str = r_str.rstrip(", ")+"\n"
    f3.write(r_str)

f2.close()
f3.close()
