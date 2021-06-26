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
        print(self.items[-1])
        return self.items.pop()

    def pop_back(self):
        print(self.items[0])
        return self.items.pop(0)

    def front(self):
        return self.items[-1]

    def back(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []

deq = Deque()
while True:
    command = str(input()).split()

    if len(command) == 1:
        command = command[0]
    if len(command) == 2:
        command, num = command
    
    if command == "push_front":
        deq.push_front(num)
        print("ok")
    
    if command == "push_back":
        deq.push_back(num)
        print("ok")

    if command == "size":
        print(deq.size())
    
    if command == "clear":
        deq.clear()
        print("ok")

    if command == "exit":
        print("bye")
        break

    
    if command == "pop_front":
        if deq.isEmpty() == False:
            deq.pop_front()
        else:
            print("error")
    if command == "pop_back":
        if deq.isEmpty() == False:
            deq.pop_back()
        else:
            print("error")
    if command == "front":
        if deq.isEmpty() == False:
            print(deq.front())
        else:
            print("error")
    if command == "back":
        if deq.isEmpty() == False:
            print(deq.back())
        else:
            print("error")