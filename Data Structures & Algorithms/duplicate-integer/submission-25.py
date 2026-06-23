class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #store in the set to keep track of duplicate
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        





        