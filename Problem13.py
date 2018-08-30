# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).

# Stack class


class Stack:

    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def isempty(self):
        return len(self.s) == 0


def isvalid(string):
    # We turn the string into a list of chars
    brackets = list(string)
    # We create the stack
    s = Stack()
    # Check to see if the stack empty and if the string is greater than 1
    if not s.isempty() and len(string) < 1:
        # If not we return false
        return False
    # We check every item in the list
    for item in brackets:
        # We check to see if it's an opening bracket
        if open(item):
            # If it is then we place it onto the stack
            s.push(item)
        else:
            # If not we check to see if it matches with its other half
            if not matches(item, s.pop()):
                # If not then we return false
                return False
    # In the end we check to see if the stack is empty if it's not then something didn't have match
    if not s.isempty():
        # We return false if that is the case
        return False
    # If everything has passed then the string must be valid
    return True


def matches(closing, opening):
    if(opening == '(' and closing != ')') or (opening == '{' and closing != '}') or (opening == '[' and closing != ']'):
        return False
    return True


def open(item):
    if item == '(' or item == '[' or item == '{':
        return True
    return False


def main():
    string = "()((()))()"
    print(isvalid(string))


main()
