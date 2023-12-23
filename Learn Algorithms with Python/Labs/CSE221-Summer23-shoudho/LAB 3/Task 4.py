f1 = "input.txt"
f = open(f1, "r")
f2 = "output.txt"
f = open(f2, "w")

T = int(f.readline())
inp = f.readline().split()

list1= []
for i in range(T):
    list1.append(int(inp[i]))
I= int(f.readline())

list2 = []
for _ in range(I):
    list2.append(int(f.readline()))

def part(arr, l, h):
    pivot = arr[h]  
    i = l- 1  
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return i + 1  


def findmin(arr, l, h, k):
    if l== h:
        return arr[l]
    pivotInd = part(arr, l, h)  
    if k == pivotInd - l+ 1:  
        return arr[pivotInd]
    if k < pivotInd - l + 1:  #
        return findmin(arr, l, pivotInd - 1, k)
    return findmin(arr, pivotInd + 1, h, k - (pivotInd- l+ 1))  


res = []
for k in list2:
    res = findmin(list1,0,T-1, k)
    res.append(res)

for res in res:
    f.write(str(res) + "\n")
f.close()
f.close()