class Node:

    def __init__(self, n):
        self.n = n
        next = None


def intersect(h1, h2):
    current1 = h1
    current2 = h2
    datalist = {}

    # Check to see if the lists are not at the end
    while current1 is not None or current2 is not None:
        # We check individually which reference has reached the end of the list
        if current1 is not None:
            # If not then we check to see if the data of the node is in the dictionary
            if current1.n in datalist:
                return current1.n
            # If not then we just update the dictionary and move on to the next node
            datalist.update({current1.n: current1.n})
            current1 = current1.next
        if current2 is not None:
            if current2.n in datalist:
                return current2.n
            datalist.update({current2.n: current2.n})
            current2 = current2.next
    # If there is not intersecting data then we return no value
    return "Lists to do not have an intersecting value"


def main():

    h1 = Node(3)
    h1.next = Node(7)
    h1.next.next = Node(8)
    h1.next.next.next = Node(10)

    h2 = Node(99)
    h2.next = Node(1)
    h2.next.next = Node(8)
    h2.next.next.next = Node(10)

    print(intersect(h1, h2))


main()
