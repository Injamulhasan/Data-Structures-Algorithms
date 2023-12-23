f3 = open('input3.txt', 'r')
f4 = open('output3.txt', 'w')

def sort_students(n, id, marks):  
    students = []

    for i in range(n):
        students.append((id[i], marks[i]))

    def sort_key(student):
        return (-student[1], student[0])
    students.sort(key=sort_key)
    return students

n = int(f3.readline().strip())
id = [int(x) for x in f3.readline().strip().split()]
marks = [int(x) for x in f3.readline().strip().split()]

sorted_students = sort_students(n,id,marks)  

for student in sorted_students:
    f4.write(f"ID: {student[0]} Mark: {student[1]}\n")

f3.close()
f4.close()
