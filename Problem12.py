import re

# We use full match here because we want to see if the whole string matches the expression given


def is_a_match(s, reg):
    # If not then we return false
    if re.fullmatch(reg, s):
        return True
    return False


def main():

    print(is_a_match("ray", "ra."))  # True
    print(is_a_match("raymond", "ra."))  # False
    print(is_a_match("chat", ".*at"))  # True
    print(is_a_match("chats", ".*at"))  # False


main()



