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

def find_biggest_value(root):
    if root is None:
        return None

    if root.right is None:
        return root.val

    return find_biggest_value(root.right)

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

    print(f'Biggest is {find_biggest_value(root)}')

