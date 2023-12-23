file_a = open("input5.txt", "r")
T = int(file_a.readline())
l1 = []
input = file_a.readline().split()
for i in range(T):
    l1.append(int(input[i]))


def quick_sort(l1, l, h):
    if l < h:
        p = partition(l1, l, h)
        quick_sort(l1, l, p - 1)
        quick_sort(l1, p + 1, h)


def partition(l1, l, h):
    p = l1[h]
    i = l - 1
    for j in range(l, h):
        if l1[j] <= p:
            i += 1
            l1[i], l1[j] = l1[j], l1[i]
    l1[i + 1], l1[h] = l1[h], l1[i + 1]
    return i + 1


file_b = open("output5.txt", "w")
quick_sort(l1, 0, T - 1)
for i in range(T):
    file_b.write(str(l1[i]) + " ")


file_b.close()
file_a.close()
