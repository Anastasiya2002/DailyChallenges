from collections import deque
class Solution:
    def getUpdatedAns(self, ans, possibleAns):
        return possibleAns if ans == 0 else min(ans, possibleAns)
    
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        queue = deque()
        runningSum = 0
        ans = 0
        for num in nums:
            queue.append(num)
            runningSum += num
            while runningSum >= s:
                ans = self.getUpdatedAns(ans, len(queue))
                poppedNum = queue.popleft()
                runningSum -= poppedNum
        return ans
