class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


count = 0


def count_unival_trees(node):

    global count
    if node is None:
        return True

    leftnode = count_unival_trees(node.left)
    rightnode = count_unival_trees(node.right)

    if not leftnode or not rightnode:
        return False

    if node.left and node.data != node.left.data:
        return False

    if node.right and node.data != node.right.data:
        return False

    count += 1
    return True


def main():

    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)
    count_unival_trees(root)
    print(count)


main()
