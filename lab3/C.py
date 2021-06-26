from sys import stdin, stdout
def maxx(lst):
    maks = lst[0]
    for i in lst:
        if i > maks:
            maks = i
    return maks
n = int(stdin.readline().strip())
arr = stdin.readline().strip().split()
arr = [int(x) for x in arr]
stdout.write(str(arr.index(maxx(arr)) + 1))