# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack.
# If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently.
# If there are no elements in the stack, then it should throw an error or return null.

import sys


class Stack:

    # make the stack and a variable to store the min
    def __init__(self):
        self.s = []
        self.max = -sys.maxsize

    def push(self, item):
        # Put the value on the list
        self.s.append(item)
        # Check to see if the value is greater than the current max
        if item > self.max:
            self.max = item

    def pop(self):
        # Remove the last item on the stack
        return self.s.pop()

    def getmax(self):
        # If the list is empty then we throw and error
        if len(self.s) == 0:
            return ValueError("Nothing in stack")
        # Else we return the current max
        return self.max


def main():
    stack = Stack()
    print(stack.getmax())
    stack.push(12)
    stack.push(124)
    stack.push(0)
    stack.push(67)
    print(stack.getmax())


main()
