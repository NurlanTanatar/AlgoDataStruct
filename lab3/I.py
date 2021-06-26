from sys import stdin, stdout

def find_left(arr, elem):
    l = -1
    r = len(arr)
    while r > l + 1:
        m = int((l + r) / 2)
        if arr[m] <= elem:
            l = m
        else:
            r = m
    return l

def find_right(arr, elem):
    l = -1
    r = len(arr)
    while r > l + 1:
        m = int((l + r) / 2)
        if arr[m] < elem:
            l = m
        else:
            r = m
    return r

n = stdin.readline()

N = stdin.readline().strip().split()
N = [int(x) for x in N]

K = stdin.readline().strip().split()
K = [int(x) for x in K]

for i in K:
    num = find_left(N, i)
    if num >= 0 and N[num] == i :
        stdout.write(f"{find_right(N, i) + 1} {find_left(N, i) + 1}\n")
    else:
        stdout.write("0\n")