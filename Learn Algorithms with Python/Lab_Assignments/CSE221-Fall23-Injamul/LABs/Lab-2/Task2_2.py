input_file = open("input2_2.txt", "r")

elem = input_file.readlines()

a = int(elem[0])
b = int(elem[2])
l1 = []
num1 = elem[1].split()
for i in range(a):
    l1.append(int(num1[i]))

l2 = []
num2 = elem[3].split()
for i in range(b):
    l2.append(int(num2[i]))

def Merge(l1, l2, a, b):
    r = [0] * (a + b)
    i, j = a - 1, b - 1
    k = a + b - 1
    while i >= 0 and j >= 0:
        if l1[i] > l2[j]:
            r[k] = l1[i]
            i -= 1
        else:
            r[k] = l2[j]
            j -= 1
        k -= 1
    while i >= 0:
        r[k] = l1[i]
        i -= 1
        k -= 1
    while j >= 0:
        r[k] = l2[j]
        j -= 1
        k -= 1
    return r



output_file = open("output2_2.txt", "w")

m = Merge(l1, l2, a, b)
res = ""
for i in range(len(m)):
    res += str(m[i]) + " "
output_file.write(res.strip() + "\n")

input_file.close()
output_file.close()
