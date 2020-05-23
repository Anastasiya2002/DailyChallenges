#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
#Return the sum of the three integers. You may assume that each input would have exactly one solution.
def threeSumClosest(nums,target):
    nums.sort()
    found_target = sum(nums[:3])
    previous =  sum(nums[:3])
    for i in range(len(nums)-1):
        left = i+1
        right = len(nums)-1
        while left < right:
            got_target = nums[i] + nums[left] + nums[right]
            if got_target > target:
                    right -= 1
            elif got_target < target:
                    left+= 1
            else:
                return got_target

            targets= [abs(target-previous), abs(target- got_target), abs(target - found_target)]
            found = min(targets)
            index = targets.index(found)
            found_target = previous if index == 0 else got_target if index == 1 else found_target 
            previous = got_target
    return found_target

print(threeSumClosest([-1,2,1,-4],1))

            
