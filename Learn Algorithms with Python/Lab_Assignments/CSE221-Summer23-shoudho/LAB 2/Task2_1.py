#O(n)
f1 = open("input2_1.txt", "r")
f2 = open("output2_1.txt", "w")
T= f1.readlines()

a =int(T[0])
b= int(T[2])
list1 = []
num =T[1].split()
for i in range(a):
    list1.append(int(num[i]))

list2 = []
numbers =T[3].split()
for i in range(b):
    list2.append(int(num[i]))

def Merge(list1,list2,a,b):
    r = [0]*(a +b)
    i, j = a-1,b-1
    k = a +b - 1
    while i>=0 and j>=0:
        if list1[i] > list2[j]:
            r[k] =list1[i]
            i-=1
        else:
            r[k] =list2[j]
            j-=1
        k-=1
    while i>=0:
        r[k]=list1[i]
        i-=1
        k-=1
    while j>=0:
        r[k]=list2[j]
        j-=1
        k-=1
    return r

result=Merge(list1,list2,a,b)
output=""
for i in range(len(result)):
    output += str(result[i]) + " "
f2.write(output.strip()+"\n")

f1.close()
f2.close()

