file_a = "input4.txt"


def findmaxval(num):
    T = len(num)
    n = float('-inf')
    s = float('-inf')

    for i in range(T - 1, -1, -1):
        s = max(s, num[i] + n)
        n = max(n, num[i] ** 2)

    return s


def fileread(file_a):
    file = open(file_a, "r")
    T = int(file.readline())
    n_inp = file.readline().split()
    l1 = []

    for k in range(T):
        l1.append(int(n_inp[k]))
    file.close()

    return T, l1


file_b = "output4.txt"


def write(file_b, out_p):
    f = open(file_b, "w")
    f.write(str(out_p))
    f.close()


T, lst = fileread(file_a)

res = findmaxval(lst)
write(file_b, res)
