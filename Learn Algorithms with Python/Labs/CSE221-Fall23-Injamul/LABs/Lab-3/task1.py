file_a = open('input1.txt', 'r')
T = int(file_a.readline())
l = []
val = file_a.readline().split()
for i in range(T):
    l.append(int(val[i]))


def Merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def MergeSort(l):
    if len(l) <= 1:
        return l
    else:
        mid = len(l) // 2
        l1 = MergeSort(l[:mid])
        l2 = MergeSort(l[mid:])
        return Merge(l1, l2)


file_b = open('output1.txt', 'w')
m = MergeSort(l)
for i in range(len(m)):
    file_b.write(str(m[i]))
    if i != len(m) - 1:
        file_b.write(",")

file_a.close()
file_b.close()
