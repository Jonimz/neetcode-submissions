class Solution:
    def getConcatenation(self, nums):
        n=len(nums)
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num) #append num to ans
        return ans