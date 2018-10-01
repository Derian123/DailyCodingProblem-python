# Given the head of a singly linked list, reverse it in-place.


class Node:

    # Node class
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(head):
    # If it is null return it
    if head is None:
        return head

    # We make references to the current node and for the node before it
    current = head
    previous = None

    # We continue until current is null
    while current is not None:
        # The reference to the next node will be the node after current
        nodenext = current.next
        # the current node's reference will be changed to point to previous, the node before current
        current.next = previous
        # previous moves down the list to consider that node the next previous node
        previous = current
        # current moves down the list to consider that node the next current node
        current = nodenext

    # the head of the linked list changes to point to previous after since previous will be at the end of the list
    head = previous
    # return the new head reference
    return head


# prints out the linked list
def printll(head):
    runner = head

    while runner is not None:
        print(runner.data)
        runner = runner.next


def main():
    head = Node(10)
    head.next = Node(11)
    head.next.next = Node(1256)
    head.next.next.next = Node(90)

    head = reverse(head)
    printll(head)


main()
