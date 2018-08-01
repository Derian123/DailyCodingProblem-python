# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.


# We know to get the number of steps it's n-2 + n-1 with 0 and 1 being equal to 1.
# we go throughout the for loop and the last index it the amount of unique ways


def number_of_ways(steps):
    numlist = [1, 1]
    for i in range(2, steps+1):
        numlist.append(numlist[i-2] + numlist[i-1])
    return numlist[steps]


def main():
    steps = 4
    print(number_of_ways(steps))


main()
