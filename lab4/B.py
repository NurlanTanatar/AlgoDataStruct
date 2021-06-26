from sys import stdin, stdout

class Node:
    def __init__(self, pnt):
        self.data = pnt
        self.r = None
        self.l = None

def insert(root, pnt):
    if root is None:
        return Node(pnt)
    else:
        if root.data == pnt:
            return root
        elif root.data < pnt:
            root.r = insert(root.r, pnt)
        else:
            root.l = insert(root.l, pnt)
    return root

def count(node):
    if node is None:
        return 0
    else:
        left_depth = count(node.l)
        right_depth = count(node.r)    
        return 1 + left_depth + right_depth

arr = list(map(int, stdin.readline().strip().split()))[:-1]
parent = Node(arr[0])
del arr[0]
for i in arr:
    insert(parent,i)
stdout.write(str(count(parent)))