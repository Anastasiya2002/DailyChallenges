#Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#Note:
#The solution set must not contain duplicate triplets.
def treeSum(nums):
    arr=[]
    for i in range(len(nums)-1):
        nums.sort()
        length = len(nums)
        result = []
        for i in range(length-2):
            left = i+1
            right = length-1
            while left < right:
                sum_value = nums[i]+nums[left]+nums[right]
                if sum_value == 0:
                    if [nums[i],nums[left],nums[right]] not in result:
                        result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                elif sum_value < 0:
                    left +=1
                else:
                    right -= 1
        return result

print(treeSum([-1,0,1,2,-1,4]))