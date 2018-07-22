#Python answer
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

#The first method is most efficient since it only goes through the list one time
def array_has_some_of(numlist, target):
    nums = {}
    #We go through the list one by one
    for num in numlist:
        #if the compliment of the current num is in the dictionary then it exisits
        if target-num in nums:
            return True
        #Else we update the dictionary to contain that value
        nums.update({num : num})
    #If the loop has finished then the pair does no exist
    return False

#This way isn't the best way but it still works
def inef_array_has_some_of(numlist,target):
    #nested for loop to go through all possible combinations
    for i in range(0,len(numlist)-1):
        for j in range(i+1, len(numlist)):
            #We always check to see if the current indices equal to the target
            if numlist[i] + numlist[j] == target:
                return True
    #If the loop finishes then there is no way to reach the target
    return False

def main():
    numlist = [10,15,3,7]
    print(array_has_some_of(numlist,17))
    print(inef_array_has_some_of(numlist,17))
main()