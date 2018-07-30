# Given a list of integers,
# write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.

#This method find the largest sum by finding the sum of previous numbers that are not adjacent
#And comparing it to the current sum of non adjacent numbers


def largest_sum(numlist):
    current_sum = 0
    previous_sum = 0
    for num in numlist:
        if previous_sum > current_sum:
            temp_sum = previous_sum
        else:
            temp_sum = current_sum
        current_sum = previous_sum + num
        previous_sum = temp_sum
    if previous_sum > current_sum:
        return previous_sum
    return current_sum


def main():
    numlist = [2, 4, 6, 2, 5]
    print(largest_sum(numlist))


main()
