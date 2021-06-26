from sys import stdin, stdout

from collections import deque
fst, snd = deque(), deque()

stop = int(input())

while stop > 0:
    stop -= 1
    command =  stdin.readline().strip().split()

    if len(command) == 1:
        command = command[0]
    if len(command) == 2:
        command, num = command
    
    if command == "+":
        snd.appendleft(num)
    if command == "*":
        snd.append(num)
    if command == "-":
        stdout.write(f"{fst[-1]}\n")
        fst.pop()
    if len(snd) > len(fst):
        fst.appendleft(snd[-1])
        snd.pop()


