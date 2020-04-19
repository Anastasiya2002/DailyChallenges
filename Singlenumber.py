#easy and a fast way to find the number that is not repeating in an arry
import collections 
class Solution:
    def singleNumber(self,nums:List[int]):
       c = collections.Counter(nums)
       print(list(c.keys())[list(c.values()).index(1)])
