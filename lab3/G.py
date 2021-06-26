from sys import stdin, stdout

def find(arr, elem):
    l = 0
    r = len(arr) - 1
    while r >= l:
        m = int((l + r) / 2)
        if arr[m] == elem:
            return True
        if arr[m] < elem:
            l = m + 1
        if arr[m] > elem:
            r = m - 1
    return False

k = stdin.readline()

N = stdin.readline().strip().split()
N = [int(x) for x in N]

K = stdin.readline().strip().split()
K = [int(x) for x in K]

for i in K:
    stdout.write("YES\n") if find(N, i) else stdout.write("NO\n")

