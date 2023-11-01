f = open("input2.txt", "r")
T = int(f.readline().strip())
f.close()

ar = [0] * (T+ 1)
ar[0] = 1

for i in range(1,T+ 1):

    if i >= 1:

        ar[i] +=ar[i - 1]
    if i >= 2:
        
        ar[i] +=ar[i - 2]

f1 = open("output2.txt", "w")
f1.write(str(ar[T]))
f1.close()




