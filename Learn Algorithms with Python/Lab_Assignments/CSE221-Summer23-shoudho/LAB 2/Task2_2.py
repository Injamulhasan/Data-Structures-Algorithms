#O(nlogn)
f1 = open("input2_2.txt", "r")
f2 = open("output2_2.txt", "w")
T = f1.readlines()

a = int(T[0])
b = int(T[2])
list1 = []
num = T[1].split()
for i in range(a):
    list1.append(int(num[i]))

list2 = []
num2 = T[3].split()
for i in range(b):
    list2.append(int(num2[i]))

def MergeSort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = MergeSort(list[:mid])
    right = MergeSort(list[mid:])
    return Merge(left, right)

def Merge(left, right):
    list3 = []
    i = j = 0
    while i<len(left) and j < len(right):
        if left[i]<right[j]:
            list3.append(left[i])
            i+=1
        else:
            list3.append(right[j])
            j+=1
    while i<len(left):
        list3.append(left[i])
        i+=1
    while j < len(right):
        list3.append(right[j])
        j+=1
    return list3

r1 = MergeSort(list1)
r2 = MergeSort(list2)
list3 = Merge(r1,r2)
output = ""
for i in range(len(list3)):
    output += str(list3[i])
    if i!=len(list3) - 1:
        output += " "
output += "\n"
f2.write(output)

f1.close()
f2.close()
