#You are given a circular array nums of positive and negative integers. If a number k at an index is positive, then move forward k steps. Conversely, if it's negative (-k), move backward k steps. Since the array is circular, you may assume that the last element's next element is the first element, and the first element's previous element is the last element.
#Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction. In other words, a cycle must not consist of both forward and backward movements.
 
def circularArrayLoop(nums):
    for i in range(len(nums)):
        step = i
        previous = i
        length= 0
        while (nums[previous] > 0 and nums[step]>0) or(nums[previous] < 0 and nums[step]<0):
            previous = step
            step += nums[step]
            if step >= len(nums):
                step = step- len(nums)
            elif step < 0:
                step = len(nums)+step
            if step == i:
                if previous != step:
                  return True
                else:
                    break
    return False

print(circularArrayLoop([2,-1,1,2,2]))

