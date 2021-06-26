from sys import stdin, stdout
num = stdin.readline()
arr = list(set(map(int, stdin.readline().strip().split()))).sort()
stdout.write(str((arr[-2])))