f = open("input1.txt", "r")
f1 = open("output1.txt", "w")
T = int(f.readline())

h = []
h_inp = f.readline().split()
for i in range(T):
    h.append(int(h_inp[i]))


def alien_comp(h):

    count=0

    for i in range(len(h)):
        for j in range(i+1,len(h)):
            if h[i]>h[j]:
                count+=1
    return count

count = alien_comp(h)
f1.write(str(count))
f.close()
f1.close()
