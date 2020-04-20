def moveZeroes(nums):
    count = nums.count(0)
    for i in range(count):
        nums.remove(0) 
    
    nums += [0 for i in range(count)]

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)