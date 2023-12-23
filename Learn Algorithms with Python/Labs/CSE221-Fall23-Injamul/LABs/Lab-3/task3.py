file_a = open("input3.txt", "r")
T = int(file_a.readline())

h = []
h_inp = file_a.readline().split()
for i in range(T):
    h.append(int(h_inp[i]))


def alien(h):
    count = 0

    for i in range(len(h)):
        for j in range(i + 1, len(h)):
            if h[i] > h[j]:
                count += 1
    return count


file_b = open("output3.txt", "w")

c = alien(h)
file_b.write(str(c))
file_a.close()
file_b.close()
