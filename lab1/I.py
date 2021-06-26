from sys import stdin, stdout

num = int(stdin.readline().strip())

stek = [[]] * 501

for i in range(num):
    cont = int(stdin.readline().strip())
    for _ in range(cont):
        n = int(stdin.readline().strip())
        stek[i].append(n)