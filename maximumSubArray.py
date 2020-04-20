#Given an integer array nums, find the contiguous subarray 
#containing at least one number) which has 
#the largest sum and return its sum.

def maxSubArray(nums):
    max_largest= 0
    for i in range(len(nums)):
        for j in range(len(nums), i,-1):
            print(nums[i:j])
            if sum(nums[i:j]) >max_largest or (i == 0 and j == len(nums)):
                max_largest= sum(nums[i:j])
    return max_largest
print(maxSubArray([-1]))