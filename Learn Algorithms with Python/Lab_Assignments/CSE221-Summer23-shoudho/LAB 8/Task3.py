def minC(cn, amt):

    cn.sort()
    ar= [float('inf')]*(amt + 1)
    ar[0] = 0
    
    for i in range(1, amt + 1):

        for c in cn:

            if c<= i:
                ar[i] = min(ar[i],ar[i -c] + 1)
    
    return ar[amt] if ar[amt] != float('inf') else -1

def r_inp(f3):

    f = open(f3, 'r')
    a,b = map(int, f.readline().split())
    c_val = list(map(int, f.readline().split()))
    f.close()

    return c_val,b

def w_out(res, f3):
    
    f = open(f3, 'w')
    f.write(str(res))
    f.close()

f3 = "input3.txt"
c_val, tgt_amt = r_inp(f3)
res= minC(c_val,tgt_amt)
f3 = "output3.txt"
w_out(res, f3)
