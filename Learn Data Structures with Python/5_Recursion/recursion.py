def printList(h):
    t = h
    while t != None:
        print(t.elem,end=" ")
        t = t.next
    print()
class Node:
    def __init__(self, e, n):
        self.elem = e
        self.next = n
#For Ascending
l1 = [10, 25, 30, 40]
l2 = [5, 7, 20, 27]

#For Descending
l3 = [40, 30, 25, 10]
l4 = [27, 20, 7, 5]

h1 = Node(l1[0], None)
tail = h1
for i in range(1, len(l1)):
    n = Node(l1[i], None)
    tail.next = n
    tail = tail.next

h2 = Node(l2[0], None)
tail = h2
for i in range(1, len(l2)):
    n = Node(l2[i], None)
    tail.next = n
    tail = tail.next
printList(h1)
printList(h2)

h3 = Node(l3[0], None)
tail = h3
for i in range(1, len(l3)):
    n = Node(l3[i], None)
    tail.next = n
    tail = tail.next

h4 = Node(l4[0], None)
tail = h4
for i in range(1, len(l4)):
    n = Node(l4[i], None)
    tail.next = n
    tail = tail.next
printList(h3)
printList(h4)

def sortedMergeAscending(h1, h2, newHead):
    if h1 is None:
        return h2
    elif h2 is None:
        return h1
    if h1.elem <= h2.elem:
        newHead = h1
        newHead.next = sortedMergeAscending(h1.next, h2, newHead)
    else:
        newHead = h2
        newHead.next = sortedMergeAscending(h1, h2.next, newHead)

    return newHead

nH = sortedMergeAscending(h1, h2, None)
printList(nH)

def sortedMergeDescending(h1, h2, newHead):
    if h1 is None:
        return h2
    elif h2 is None:
        return h1
    if h1.elem >= h2.elem:
        newHead = h1
        newHead.next = sortedMergeDescending(h1.next, h2, newHead)
    else:
        newHead = h2
        newHead.next = sortedMergeDescending(h1, h2.next, newHead)

    return newHead

nH = sortedMergeDescending(h3, h4, None)
printList(nH)