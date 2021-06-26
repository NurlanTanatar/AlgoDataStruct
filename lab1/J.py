from sys import stdin, stdout

def gcd(a, b):
    while(b):
       a, b = b, a % b
    return a

# def lcm(a, b):
#     return (a * b) / gcd(a, b)

a = int(stdin.readline().strip())
b = int(stdin.readline().strip())
stdout.write(str(gcd(a, b)))