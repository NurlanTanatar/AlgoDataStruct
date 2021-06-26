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

def print_tree(node):
    if node.l:
        print_tree(node.l)
    stdout.write(str(node.data) + '\n'),
    if node.r:
        print_tree(node.r)

arr = list(map(int, stdin.readline().strip().split()))[:-1]
parent = Node(arr[0])
del arr[0]
for i in arr:
    insert(parent,i)
print_tree(parent)