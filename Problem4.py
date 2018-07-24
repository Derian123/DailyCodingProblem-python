# Given an array of integers, find the first missing positive integer.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.


def find_next_positive_missing_integer(numlist):
    if len(numlist) == 0:
        return
    numlist.sort()
    next_index = 1
    for i in range(len(numlist)-1):
        if numlist[i] < 0:
            next_index += 1
        elif numlist[i] + 1 != numlist[next_index]:
            return numlist[i] + 1
        next_index += 1
    return numlist[-1] + 1


def main():
    numlist = []
    print(find_next_positive_missing_integer(numlist))


main()
