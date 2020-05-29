#Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
def nextPermutation(nums) :
    if len(nums) <= 1:
            return nums
        # Find first decreasing element from end
    i = len(nums) - 2
    while i >=0 and nums[i] >= nums[i+1]:
            i -= 1
    if i >= 0:
            # find fisrt number larger than first decreasing from the end
        j = len(nums)-1
        while j >= i and nums[j] <= nums[i]:
            j -= 1
            # swap values
            nums[i], nums[j] = nums[j], nums[i]
        # revert part of list
    nums[i+1:] = reversed(nums[i+1:])
    return nums
print(nextPermutation([1,1,5]))
