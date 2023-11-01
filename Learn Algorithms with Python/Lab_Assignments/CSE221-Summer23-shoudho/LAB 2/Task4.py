
f1=open('input4.txt', 'r')
f2=open('output4.txt', 'w')

T = int(f1.readline())
list1=[]
val = f1.readline().split()
for i in range(T):
    list1.append(int(val[i]))

def find_max(arr,s,e):
    if s == e:
        return arr[s]
    
    mid = (s+e) // 2
    l_max=find_max(arr,s,mid)
    r_max=find_max(arr,mid+1,e)
    return max(l_max,r_max)
max_val = find_max(list1,0,T-1)
f2.write(str(max_val))

f1.close()
f2.close()
