class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        # we have to use a dictionary 
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return[seen[needed], i]
            seen[nums[i]] = i
        return []