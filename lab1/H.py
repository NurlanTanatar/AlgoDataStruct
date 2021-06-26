class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push_front(self, item):
        self.items.append(item)

    def push_back(self, item):
        self.items.insert(0,item)

    def pop_front(self):
        return self.items.pop()

    def pop_back(self):
        return self.items.pop(0)

    def front(self):
        return self.items[-1]

    def back(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []

fst, snd = Deque(), Deque()

stop = int(input())

while stop > 0:
    stop -= 1
    command = str(input()).split()

    if len(command) == 1:
        command = command[0]
    if len(command) == 2:
        command, num = command
    
    if command == "+":
        snd.push_back(num)
    if command == "*":
        snd.push_front(num)
    if command == "-":
        print(f"{fst.front()}\n")
        fst.pop_front()
    if snd.size() > fst.size():
        fst.push_back(snd.front())
        snd.pop_front()


