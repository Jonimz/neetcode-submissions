class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # num_set = set(nums)
        n = len(nums)
        expec_length = n * (n + 1) // 2
        act_length = sum(nums)
        return  expec_length - act_length
        