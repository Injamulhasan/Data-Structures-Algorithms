file_a = open('input2.txt', 'r')
T = int(file_a.readline())

l = []
value = file_a.readline().split()

for i in range(T):
    l.append(int(value[i]))


def find_max(x, s, e):
    if s == e:
        return x[s]

    mid = (s + e) // 2
    l_max = find_max(x, s, mid)
    r_max = find_max(x, mid + 1, e)
    return max(l_max, r_max)


file_b = open('output2.txt', 'w')
max = find_max(l, 0, T - 1)
file_b.write(str(max))

file_a.close()
file_b.close()
