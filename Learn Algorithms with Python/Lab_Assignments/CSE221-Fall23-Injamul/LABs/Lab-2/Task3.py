f1 = open('input3.txt', 'r')
N = int(f1.readline())
list1 = []
for i in range(N):
    start, end = map(int, f1.readline().split())
    list1.append((start, end))


def maxtasks(tasks):
    tasks.sort(key=lambda x: x[1])
    selected_tasks = []
    last_end_time = -1

    for task in tasks:
        start_time, end_time = task
        if start_time > last_end_time:
            selected_tasks.append((start_time, end_time))
            last_end_time = end_time

    return selected_tasks


f2 = open('output3.txt', 'w')
selected_tasks = maxtasks(list1)

f2.write(str(len(selected_tasks)) + "\n")
for task in selected_tasks:
    f2.write(f"{task[0]} {task[1]}\n")

f1.close()
f2.close()
