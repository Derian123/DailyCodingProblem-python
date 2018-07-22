# Given an array of integers, return a new array
# such that each element at index i of the new array is the product
# of all the numbers in the original array except the one at i.
#
# This approach finds the total of all indices and divides each number by that total.


def product_of_all_indices(numlist):
    result = 1
    newlist = []
    for num in numlist:
        result *= num
    for num in numlist:
        newlist.append(result/num)
    return newlist


# This approach does the same problem without division
# We start from the left to get all the outcomes of the indicies before it
# Then we start from the right to get those indices that came after the number


def without_division_product_of_all_indices(numlist):
    result = 1
    newlist = []
    for num in numlist:
        newlist.append(result)
        result *= num
    result = 1
    for i in range(len(numlist)-1, -1, -1):
        newlist[i] *= result
        result *= numlist[i]
    return newlist


def main():
    numlist = [1, 2, 3, 4, 5]
    print(product_of_all_indices(numlist))
    print(without_division_product_of_all_indices(numlist))


main()
