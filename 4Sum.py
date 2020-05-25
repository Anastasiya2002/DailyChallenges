#Given an array nums of n integers and an integer target, 
# are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

def fourSum(nums,target):
    nums.sort()
    quadruplets = []
    for i in range(len(nums)-3):
        for second in range(i+1,len(nums)-2):
           left = second+1
           right = len(nums)-1
           while left<right:
              quadruplet = [nums[i],nums[second],nums[left],nums[right]]
              new_target = sum(quadruplet)
              if new_target == target:
                  if quadruplet not in quadruplets:
                      quadruplets.append(quadruplet)
                  left += 1
                  right -= 1
              elif new_target > target:
                  right -= 1
              else:
                  left+= 1
             
    return quadruplets
print(fourSum([1,0,-1,0,-2,2],0))