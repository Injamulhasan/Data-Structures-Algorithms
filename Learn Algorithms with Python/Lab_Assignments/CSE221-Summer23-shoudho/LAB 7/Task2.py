def max_t(t, I):
    t.sort(key=lambda x: x[1])  
    a= [0]*I 
    c = 0

    for tk in t:
        st, end = tk
        assign = None
        for i in range(I):
            if a[i] <= st:
                assign = i
                break
        if assign is not None:
            a[assign] = end  
            c+= 1
    return c

def r_inp(f3):
    f = open(f3, 'r')
    a,b = map(int,f.readline().split())
    t = []
    for _ in range(a):
        st, end = map(int,f.readline().split())
        t.append((st, end))
    f.close()
    return t,b

def w_out(out, f3):
    f = open(f3, 'w')
    f.write(str(out))
    f.close()


t,b = r_inp("input2.txt")
res = max_t(t,b)
print(res)
w_out(res,"output2.txt")
