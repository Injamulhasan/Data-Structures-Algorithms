#(nlogn)
f1 = open("input1_2.txt", "r")
f2 = open("output1_2.txt", "w")

T = f1.readlines()
a, b = T[0].split()
a = int(a)
b = int(b)

num = T[1].split()
for i in range(a):
   num[i] = int(num[i])
ind = [(num[i], i) for i in range(a)]

def Merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = Merge_sort(arr[:mid])
    right = Merge_sort(arr[mid:])
    return Merge(left, right)

def Merge(left, right):
    list1=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i][0] < right[j][0]:
            list1.append(left[i])
            i+=1
        else:
            list1.append(right[j])
            j+=1

    while i<len(left):
        list1.append(left[i])
        i += 1
    while j<len(right):
        list1.append(right[j])
        j += 1
    return list1

index=Merge_sort(ind)


ind1=ind2 =-1
for i in range(a):
    r=b-index[i][0]
    left = i+1
    right = a-1
    while left <= right:
        mid=left + (right - left) // 2
        if index[mid][0] == r:
            ind1 = index[i][1]
            ind2 = index[mid][1]
            break
        elif index[mid][0]<r:
            left=mid+1
        else:
            right=mid-1
    if ind1!=-1 and ind2!=-1:
        break

if ind1==-1 and ind2==-1:
    f2.write("IMPOSSIBLE\n")
else:
    f2.write(str(ind1+1) + " " + str(ind2+1) + "\n")

f1.close()
f2.close()
