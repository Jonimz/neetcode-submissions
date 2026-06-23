class Solution:
    def hasDuplicate(self, nums):
        #create a set
        seen = set()
        #loop through the numers
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False