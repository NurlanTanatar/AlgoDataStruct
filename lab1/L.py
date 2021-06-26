from sys import stdin, stdout

def gcd(x,y):
	return gcd (y, x % y) if y else x

def lcm (x,y):
	return int(x / gcd (x, y) * y)

a, b =  stdin.readline().strip().split()

stdout.write(str(lcm(int(a), int(b))))