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

nums = Stack()
params = str(input())
operators = "+-*"
tmp =[0, 0]
for i in params:
    if i.isdigit():
        nums.push(int(i))
    elif i == " ":
        pass
    else:
        tmp[0] = nums.top()
        nums.pop()
        tmp[1] = nums.top()
        nums.pop()

        if i == operators[0]:
            nums.push(tmp[1] + tmp[0])
        if i == operators[1]:
            nums.push(tmp[1] - tmp[0])
        if i == operators[2]:
            nums.push(tmp[1] * tmp[0])
        
print(nums.top())


    
