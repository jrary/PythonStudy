import sys


def preorder(a, root_num):
    if root_num == -1:
        return 0
    left, right = -1, -1
    for i in range(len(a)):
        if a[i][0] == a[root_num][1]:
            left = i
        if a[i][0] == a[root_num][2]:
            right = i
    print(a[root_num][0], end='')
    preorder(a, left)
    preorder(a, right)


def inorder(a, root_num):
    if root_num == -1:
        return 0
    left, right = -1, -1
    for i in range(len(a)):
        if a[i][0] == a[root_num][1]:
            left = i
        if a[i][0] == a[root_num][2]:
            right = i
    inorder(a, left)
    print(a[root_num][0], end='')
    inorder(a, right)


def postorder(a, root_num):
    if root_num == -1:
        return 0
    left, right = -1, -1
    for i in range(len(a)):
        if a[i][0] == a[root_num][1]:
            left = i
        if a[i][0] == a[root_num][2]:
            right = i
    postorder(a, left)
    postorder(a, right)
    print(a[root_num][0], end='')


n = int(sys.stdin.readline())
tree = []
for _ in range(n):
    tree.append(sys.stdin.readline().strip().split(' '))
preorder(tree, 0)
print("")
inorder(tree, 0)
print("")
postorder(tree, 0)
print("")
