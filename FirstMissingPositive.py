#Given an unsorted integer array, find the smallest missing positive integer.
def  firstMisiingPositive(nums):
    ans = len(nums)+1
    for i in range(len(nums),0,-1):
        if i not in nums:
            ans = i
    return ans


print(firstMisiingPositive([]))