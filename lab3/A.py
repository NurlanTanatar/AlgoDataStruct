from sys import stdin, stdout
n = int(stdin.readline().strip())
arr = stdin.readline().strip().split()
x = stdin.readline().strip()
for i in range(n):
    if x == arr[i]:
        stdout.write(str(i + 1) + '\n')