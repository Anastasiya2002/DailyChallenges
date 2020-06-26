#Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

#Note: You are not suppose to use the library's sort function for this problem.
def sortColors(nums):
    start, end = 0 , len(nums)-1
    i = 0
    while i <= end:
            if nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1 # You can't move i here since the nums[end] we swapped can be 1 or 2 , therefore we need check again at i
            elif nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                i+=1 
            else:
                i+= 1
    return nums

print(sortColors([2,0,2,1,1,0]))