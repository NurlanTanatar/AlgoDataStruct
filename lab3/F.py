from sys import stdin, stdout
arr = stdin.readline().strip().split()
arr = [int(x) for x in arr[1:]]
mini = min(arr)
maxi = max(arr)
array = [mini if i == maxi else i for i in arr]
for i in array:
    stdout.write(str(i) + ' ')
