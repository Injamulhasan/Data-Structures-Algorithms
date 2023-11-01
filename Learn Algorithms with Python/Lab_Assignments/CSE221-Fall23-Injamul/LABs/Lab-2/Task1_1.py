input_file = open("input1_1.txt", "r")
ar1 = input_file.readline().strip().split()

for i in range(len(ar1)):
    ar1[i] = int(ar1[i])

N, S = ar1[0], ar1[1]

el = input_file.readline().strip().split()


for i in range(N):
    el[i] = int(el[i])

found = False
for i in range(len(el)):
    if found == True:
        break
    for j in range(i+1, len(el)):
        if el[i] + el[j] == S:
            index1 = i + 1
            index2 = j + 1
            found = True
            break


output_file = open("output1_1.txt", mode = 'w')
if found == True:
    print(f"{index1} {index2}", file = output_file)
else:
    print(f"IMPOSSIBLE", file = output_file)

output_file.close()