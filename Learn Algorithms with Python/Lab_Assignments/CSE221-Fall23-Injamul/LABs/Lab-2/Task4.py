f1 = open('input4.txt', 'r')
N, M = map(int, f1.readline().split())
tasks = []
for _ in range(N):
    start, end = map(int, f1.readline().split())
    tasks.append((start, end))

tasks.sort()


def merge(tasks, left, mid, right):
    i = left
    j = mid + 1
    merged = []
    count = 0

    while i <= mid and j <= right:
        if tasks[i][1] <= tasks[j][1]:
            merged.append(tasks[i])
            count += (j - mid - 1)
            i += 1
        else:
            merged.append(tasks[j])
            j += 1

    while i <= mid:
        merged.append(tasks[i])
        count += (j - mid - 1)
        i += 1

    while j <= right:
        merged.append(tasks[j])
        j += 1

    for i in range(len(merged)):
        tasks[left + i] = merged[i]

    return count


def mesoco(tasks, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += mesoco(tasks, left, mid)
        count += mesoco(tasks, mid + 1, right)
        count += merge(tasks, left, mid, right)
    return count


f2 = open('output4.txt', 'w')
max_tasks = mesoco(tasks, 0, len(tasks) - 1)
f2.write(str(max_tasks))

f1.close()
f2.close()
