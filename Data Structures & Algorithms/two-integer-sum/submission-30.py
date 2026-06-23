class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict={}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in seenDict:
                return[seenDict[diff], i]
            seenDict[nums[i]]=i


        