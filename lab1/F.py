class Stack:
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def check_seq(seq):
    stek = Stack()
    for i in seq:
        if i == '(' or i == '{' or i == '[':
            stek.push(i)
        else:
            if stek.is_empty():
                return False
            if i == '}' and stek.top() != '{':
                return False
            if i == ')' and stek.top() != '(':
                return False
            if i == ']' and stek.top() != '[':
                return False
            stek.pop()
        
    return stek.is_empty()

s = str(input())
if check_seq(s):
    print("yes\n")
else:
    print("no\n")