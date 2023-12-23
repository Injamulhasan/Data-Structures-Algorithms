
f1=open('input3.txt', 'r')
f2=open('output3.txt', 'w')

T=int(f1.readline())
list1=[]
val=f1.readline().split()
for i in range(T):
    list1.append(int(val[i]))

def Merge(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i<len(a):
        c.append(a[i])
        i+=1
    while j<len(b):
        c.append(b[j])
        j+=1
    return c

def MergeSort(list1):
    if len(list1)<=1:
        return list1
    else:
        mid=len(list1)//2
        l1=MergeSort(list1[:mid])
        l2=MergeSort(list1[mid:])
        return Merge(l1, l2)

r=MergeSort(list1)
for i in range(len(r)):
    f2.write(str(r[i]))
    if i!=len(r) - 1:
       f2.write(", ")

f1.close()
f2.close()
