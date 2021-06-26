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

def max_depth(node):
    if node is None:
        return 0
    else:
        left_depth = max_depth(node.l)
        right_depth = max_depth(node.r)

        if (left_depth > right_depth):
            return left_depth+1
        else:
            return right_depth+1
mp = map
lst = list
arr = lst(mp(int, stdin.readline().strip().split()))
parent = Node(arr[0])
for i in arr[1:-1]:
    insert(parent,i)
stdout.write(str(max_depth(parent)))