from random import randint

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_sum(root):
    if root is None:
        return 0

    return root.val + find_sum(root.left) + find_sum(root.right)

if __name__ == "__main__":
    root_val = randint(0, 100)
    print(root_val)
    root = Node(root_val)
    num_nodes = randint(0, 20)
    while num_nodes > 0:
        num_nodes -= 1
        i = randint(0, 100)
        print(i)
        root = insert(root, i)

    print(f'Sum is {find_sum(root)}')

