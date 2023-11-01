input_file = open("input1_2.txt", "r")
ar1 = input_file.readline().strip().split()

for i in range(len(ar1)):
    ar1[i] = int(ar1[i])

x, y = ar1[0], ar1[1]

elem = input_file.readline().strip().split()

for i in range(x):
    elem[i] = int(elem[i])

dic = {}

found = False

for i in range(x):
    try:
        dic[y - elem[i]]
        found = True
        break
    except:
        dic[elem[i]] = i + 1


output_file = open("output1_2.txt", mode='w')


if found == True:
    print(f"{dic[S - elem[i]]} {i + 1}", file=output_file)
else:
    print(f"IMPOSSIBLE", file=output_file)

output_file.close()