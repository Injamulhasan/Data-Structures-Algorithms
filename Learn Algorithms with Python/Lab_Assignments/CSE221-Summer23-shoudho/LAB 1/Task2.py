f1 = open('input2.txt', 'r')
f2 = open('output2.txt', 'w')

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]


n = int(f1.readline())
arr= []
T2 = f1.readline().split()
for i in range(len(T2)):
    arr.append(int(T2[i]))
bubbleSort(arr)

for i in range(len(arr)):
    f2.write(str(arr[i]) + ' ')


f1.close()
f2.close()

# best-case scenario
 #The bubble sort method will finish in one pass of the outer loop if the input array is already sorted in ascending order, giving it a time complexity of θ(n). 
 #Since the condition arr[j] > arr[j+1] will never be true in this case, the inner loop won't swap anything. 
 #The algorithm is therefore simplified and requires the fewest comparisons and swaps.

