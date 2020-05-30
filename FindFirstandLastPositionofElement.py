#Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#Your algorithm's runtime complexity must be in the order of O(log n).
def searchRange(nums,target):
    if len(nums)== 0:
        return [-1,-1]
    start = 0
    end = len(nums)-1
    found = 0
    if nums[start]==nums[end]==target:
        return [0,len(target)-1]
    while start <= end:
        middle = (start+end)//2
        if nums[middle] > target:
            end = middle-1
        elif nums[middle]<target:
            start = middle +1
        else:
            found = 1
            break
    if found == 0:
        return [-1,-1]
    start = middle
    end = middle
    start_found= False
    end_found= False
    while (start>=0 and nums[start]==target) or (end<=len(nums)-1 and nums[end]==target):
            if nums[start]==target:
                start -= 1
            if nums[end]==target:
                end += 1
    return [start+1,end-1]
print(searchRange([1,4],4))
print(searchRange([5,7,7,8,8,10], 8))

