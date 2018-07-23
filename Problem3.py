# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserialize the string back into the tree.

# Node Class


class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# Binary search tree insert
def binary_insert(root, node):
    if root is None:
        root = node

    else:
        if root.data > node.data:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)


# Prints the string in order
def print_inorder(root):

    if root is None:
        return

    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)


# put the nodes into a list
def serialize(root):
    s = []
    serializes(root, s)
    return s


# appends all node data onto the list
def serializes(root, s):
    if root is None:
        pass

    else:
        s.append(str(root.data))
        serializes(root.left, s)
        serializes(root.right, s)


# we read the list made from the data and insert one by one
def deserialize(file, root):
    if file is None:
        return
    file = open("nodes.txt", "r")
    line = file.readline()
    nums = line.split(" ")
    for num in nums:
        node = Node(int(num))
        binary_insert(root, node)


def main():

    s = []
    root = Node(-1)
    binary_insert(root, Node(1))
    binary_insert(root, Node(10))
    binary_insert(root, Node(5))
    binary_insert(root, Node(2))
    file = open("nodes.txt", "w+")
    s = serialize(root)
    nums = " ".join(s)
    file.write(nums)
    file.close()
    file = open("nodes.txt", "r")
    deserialize(file, root)
    print_inorder(root)


main()
