class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSet = set(nums)
        longest = 0

        for num in longestSet:
            if (num - 1) not in longestSet:
                length = 1

                while (num + length) in longestSet:
                    length += 1

                longest = max(length, longest)

        return longest




        