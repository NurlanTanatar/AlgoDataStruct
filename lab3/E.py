from sys import stdin, stdout
num = stdin.readline()
arr = list(set([int(x) for x in stdin.readline().strip().split()])).sort()
stdout.write(str((arr[-2])))