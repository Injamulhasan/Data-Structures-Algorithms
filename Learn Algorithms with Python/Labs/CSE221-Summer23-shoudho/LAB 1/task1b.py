f2 = open("input1b.txt", "r")
f3 = open("output1b.txt", "w")

T = int(f2.readline())  

for i in range(0, T):  
    line = f2.readline() 
    
    lst = line.split(" ")  
    n1 = int(lst[1])
    n2 = int(lst[3])
    operator = lst[2]

    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    else:
        result = n1 / n2

    output = f"The result of {n1} {operator} {n2} is {result}\n"
    f3.write(output)

f2.close()
f3.close()