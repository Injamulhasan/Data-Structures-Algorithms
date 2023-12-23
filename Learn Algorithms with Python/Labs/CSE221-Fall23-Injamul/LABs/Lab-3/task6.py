# f1 = "input6.txt"
# f = open(f1, "r")
# f2 = "output6.txt"
# f = open(f2, "w")
#
# T = int(f.readline())
# ipt = f.readline().split()
#
# l1 = []
# for i in range(T):
#     l1.append(int(ipt[i]))
# k = int(f.readline())
#
# l2 = []
# for _ in range(k):
#     l2.append(int(f.readline()))
#
#
# def partition(arr, l, h):
#     pivot = arr[h]
#     i = l - 1
#     for j in range(l, h):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[h] = arr[h], arr[i + 1]
#     return i + 1
#
#
# def find_smallest(x, l, h, k):
#     if l == h:
#         return x[l]
#     piv = partition(x, l, h)
#     if k == piv - l + 1:
#         return x[piv]
#     if k < piv - l + 1:
#         return find_smallest(x, l, piv - 1, k)
#     return find_smallest(x, piv + 1, h, k - (piv - l + 1))
#
#
# ans = []
# for k in l2:
#     ans = find_smallest(l1, 0, T - 1, k)
#     ans.append(ans)
#
# for ans in ans:
#     f.write(str(ans) + "\n")
#
# f.close()
# f.close()



def partition(arr, p, r):
    element = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= element:
            i += 1

            temp1 = arr[i]
            arr[i] = arr[j]
            arr[j] = temp1

    temp2 = arr[i + 1]
    arr[i + 1] = arr[r]
    arr[r] = temp2
    return i + 1


def kth_smallest(arr, l, r, K):
    pos = partition(arr, l, r)

    if (pos - l == K - 1):
        return arr[pos]

    if (pos - l > K - 1):
        return kth_smallest(arr, l, pos - 1, K)

    return kth_smallest(arr, pos + 1, r, K - pos + l - 1)


file_in = open('input6.txt', 'r')
file_out = open('output6.txt', 'w')

enum = file_in.readline()
enum = int(enum)
numl = file_in.readline().split(' ')
numarr2 = [0] * enum
for i in range(1, enum + 1):
    numarr2[i - 1] = int(numl[i - 1])

otpn = file_in.readline()
otpn = int(otpn)

for j in range(1, otpn + 1):
    k = file_in.readline()
    k = int(k)

    file_out.writelines(str(kth_smallest(numarr2, 0, enum - 1, k)) + '\n')
file_in.close()
file_out.close()