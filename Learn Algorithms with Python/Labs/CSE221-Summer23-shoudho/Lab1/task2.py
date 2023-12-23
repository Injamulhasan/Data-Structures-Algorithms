'''
Explanation
Implementation I uses recursion to find the fibonacchi number, and it Calculates the same fibonachi number 
multiple times if required..
                T(n) = T(n-1) + (n-2) + C
                =1+2+4+...+2**n
                =2*n+1
                =1+2+4+ nt
                =0(2n) [Time complexity of implementation 17]
                
Implementation 2 uses memoization technique to store fibonacchi numbers that has also been calculated. 
So the repeated sub-trees don't have to be calculated using recursion again, thus saving time.

                    Time Complexity of implementation = O(n) (linear)
                    
• Implementation 2 is for better than implementation 1. The graph in problem 26 also highlight this time complexity.

'''

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

input_file = open("input2.txt", "r")
n = int(input_file.readline().strip())
arr = [0] * n
elements = input_file.readline().strip().split()

for i in range(n):
    arr[i] = int(elements[i])

input_file.close()
sorted_arr = insertionSort(arr)

output_file = open("output2.txt", "w")

for x in sorted_arr:
    output_file.write(str(x) + " ")
    
output_file.close()


