list1 = []

f5 = open('input4.txt', 'r')
f6 = open('output4.txt', 'w')

n = int(f5.readline())

for i in range(n):
    list1.append(f5.readline().strip())


for i in range(len(list1)):
    for j in range(0, len(list1)-i-1):
        first = list1[j].split(' ')
        second = list1[j+1].split(' ')

        if first[0] > second[0]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
        elif first[0] == second[0] and first[-1] < second[-1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

for r in list1:
    f6.write(r + "\n")


f5.close()
f6.close()