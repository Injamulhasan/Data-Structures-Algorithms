f1 = "input2.txt"
f2 = "output2.txt"

def max_s_sq(nums):
    T = len(nums)
    max_n = float('-inf')
    max_s = float('-inf')
    
    for i in range(T-1,-1,-1):
        max_s = max(max_s, nums[i] + max_n)
        max_n = max(max_n, nums[i]**2)
    
    return max_s


def read(f1):
   
    file = open(f1, "r")
    T = int(file.readline())
    nums_inp = file.readline().split()
    list1 = []

    for i in range(T):
        list1.append(int(nums_inp[i]))
    file.close()

    return T,list1

def write(f2, output):
   
    f = open(f2,"w")
    f.write(str(output))
    f.close()

T,list1 = read(f1)

res = max_s_sq(list1)
write(f2,res)










