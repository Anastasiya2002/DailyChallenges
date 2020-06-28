#Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
def findDuplicate(nums):
    dict = {}
    for i in nums:
        if i in dict:
            return i
        else:
            dict[i]= 1

print(findDuplicate([3,1,3,4,2]))
    