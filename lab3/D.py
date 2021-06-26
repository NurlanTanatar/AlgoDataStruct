from sys import stdin, stdout
matx, maxi, mini = [], [0]*750, [0]*750
n, m = stdin.readline().strip().split()
n, m = int(n), int(m)
for i in range(n):
    arr = stdin.readline().strip().split()
    arr = [int(x) for x in arr]
    matx.append(arr)
for i in range(n):
    mini[i] = 1000
    for j in range(m):
        if matx[i][j] < mini[i]:
            mini[i] = matx[i][j]
for j in range(m):
    maxi[j] = -1000
    for i in range(n):
        if matx[i][j] > maxi[j]:
            maxi[j] = matx[i][j]
ans = 0
for i in range(n):
    for j in range(m):
        if matx[i][j] == mini[i] and matx[i][j] == maxi[j]:
            ans += 1

stdout.write(str(ans))
