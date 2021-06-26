from sys import stdin, stdout

def is_prime(n):
    if (n == 1):
        return False
    i = 2
    while(i * i <= n):
        if (n % i == 0):
            return False
        i += 1
    return True
n = int(stdin.readline().strip())
stdout.write("prime") if is_prime(n) else stdout.write("composite")