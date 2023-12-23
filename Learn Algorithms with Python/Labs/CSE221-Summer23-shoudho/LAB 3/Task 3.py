f1 = open("input3.txt", "r")
f2 = open("output3.txt", "w")
T = int(f1.readline())

list1 = []
inp = f1.readline().split()

for i in range(T):
    list1.append(int(inp[i]))

def quick(list1,l,h):

    if l< h:
        p = part(list1, l, h)
        quick(list1,l, p - 1)
        quick(list1, p+ 1, h)

def part(list1, l, h):
 
    p = list1[h]
    i = l-1

    for j in range(l,h):
        if list1[j]<=p:
            i+=1
            list1[i],list1[j] =list1[j],list1[i]
    list1[i+1],list1[h] =list1[h],list1[i+1]

    return i+1

quick(list1,0,T-1)

for i in range(T):
    f2.write(str(list1[i]) + " ")
f2.close()
f1.close()