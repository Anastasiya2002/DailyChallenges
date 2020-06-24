#Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
def maxProduct(nums):
    maximum = nums[0]
    for i in range(len(nums)):
        new_maximum =  1
        for j in range(i,len(nums)):
            new_maximum *= nums[j]
            maximum = max(maximum,new_maximum)
    return maximum

print(maxProduct([-2,3,-4]))
print(maxProduct([2,3,-2,4]))
print(maxProduct([-2,0,-1]))
            
