def threeSum(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            needed= -(nums[i]+nums[j])
            if needed in nums[j+1:]:
                if sorted([nums[i],nums[j],needed]) not in result:
                     result.append(sorted([nums[i],nums[j],needed]))
    return result

def threeSum(arr):
    # sort array elements
    arr.sort()
    result = []
    for i in range(0, len(arr)-1):
        # initialize left and right
        l = i + 1
        r = len(arr)- 1
        x = arr[i]
        while (l < r):
            if (x + arr[l] + arr[r] == 0):
                # print elements if it's sum is zero
                if [x,arr[l],arr[r]] not in result:
                    result.append([x,arr[l],arr[r]])
                l+=1
                r-=1
 
            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[l] + arr[r] < 0):
                l+=1
 
            # if sum is greater than zero than
            # decrement in right side
            else:
                r-=1
    return result

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,0]))