class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str({"key": self.key,
                    "left": self.left.key if self.left is not None else "None",
                    "right": self.right.key if self.right is not None else "None",
                    "height": self.height})


def print_tree(x):
    if x is None:
        return

    print_tree(x.left)
    print(x)
    print_tree(x.right)


def left_rotate(x):
    if x is None or x.right is None:
        return x

    A, B = x, x.right
    A.right, B.left = B.left, A
    return B


def right_rotate(x):
    if x is None or x.left is None:
        return x

    A, B = x.left, x
    A.right, B.left = B, A.right
    return A


def Balance(x):
    if x is None:
        return x
    elif x.left is None and x.right is None:
        update_height(x)
        return x

    if x.left is not None and x.left.height - (x.right.height if x.right is not None else -1) >= 2:
        if (x.left.right.height if x.left.right is not None else -1) > (x.left.left.height if x.left.left is not None else -1):
            x.left = left_rotate(x.left)
            update_height(x.left)
        x = right_rotate(x)

    elif x.right is not None and x.right.height - (x.left.height if x.left is not None else -1) >= 2:
        if (x.right.left.height if x.right.left is not None else -1) > (x.right.right.height if x.right.right is not None else -1):
            x.right = right_rotate(x.right)
            update_height(x.right)
        x = left_rotate(x)

    update_height(x)
    return x


def update_height(x):
    if x is None:
        return
    x.height = max(x.left.height if x.left is not None else -1,
                   x.right.height if x.right is not None else -1) + 1


def AVL_insert(x, z, T, isLeft):
    if z.key < x.key:
        if x.left is None:
            x.left = z
        else:
            AVL_insert(x.left, z, x, True)

    elif z.key > x.key:
        if x.right is None:
            x.right = z
        else:
            AVL_insert(x.right, z, x, False)

    update_height(x)

    print("-----------------------")
    print("Before balance, The current value is", x.key if x is not None else -1)
    print_tree(x)
    print("-----------------------")

    x = Balance(x)
    update_height(x.left)
    update_height(x.right)
    update_height(x)

    print("-----------------------")
    print("after balance, The current value is", x.key if x is not None else -1)
    print_tree(x)
    print("-----------------------")

    if isLeft:
        T.left = x
    else:
        T.right = x


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

T = Node("12345")

# left rotate and right rotate
#
# B.left = A
# B.right = D
# D.left = C
# D.right = E
#
# print_tree(B)
#
# T = left_rotate(B)
#
# T = right_rotate(T)
#
# print("------------")
#
# print_tree(T)


# test case 1

C.left = B
D.left = C
D.right = E

B.height = 0
C.height = 1
D.height = 2
E.height = 0

T.left = D

print_tree(D)

print("-----------")

AVL_insert(D, A, T, True)

print_tree(D)


# test case 2



