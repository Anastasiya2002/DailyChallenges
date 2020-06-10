class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            try:
                needed = target - nums[i]
                index = nums.index(needed,i+1)
                if index != i:
                   return [i,index]
            except:
                continue
        