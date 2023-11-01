f = open("input1a.txt","r")
f1 = open("output1a.txt","w")

T = int(f.readline().strip())

for i in range(T):
  current_num=int(f.readline().strip())
  if current_num%2==0:
    f1.write(f'{current_num} is an Even number.\n')
  else:
    f1.write(f'{current_num} is a Odd number.\n')

f.close()
f1.close()