input_file = open("input2_1.txt", "r")
elem = input_file.readlines()

a = int(elem[0])
b = int(elem[2])


l1 = []
num = elem[1].split()
for i in range(a):
    l1.append(int(num[i]))

l2 = []
num2 = elem[3].split()
for i in range(b):
    l2.append(int(num2[i]))

def MergeSort(l):
    if len(l) <= 1:
        return l
    mid = len(l)//2
    left = MergeSort(l[:mid])
    right = MergeSort(l[mid:])
    return Merge(left, right)

def Merge(left, right):
    l3 = []
    i = j = 0
    while i<len(left) and j < len(right):
        if left[i]<right[j]:
            l3.append(left[i])
            i+=1
        else:
            l3.append(right[j])
            j+=1
    while i<len(left):
        l3.append(left[i])
        i+=1
    while j < len(right):
        l3.append(right[j])
        j+=1
    return l3


output_file = open("output2_1.txt", "w")
r1 = MergeSort(l1)
r2 = MergeSort(l2)
l3 = Merge(r1,r2)
res = ""
for i in range(len(l3)):
    res += str(l3[i])
    if i!=len(l3) - 1:
        res += " "
res += "\n"

output_file.write(res)

input_file.close()
output_file.close()
