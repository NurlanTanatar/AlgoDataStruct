from sys import stdin, stdout
from math import ceil, log2
N = int(stdin.readline().strip())
stdout.write(str(ceil(log2(N))))