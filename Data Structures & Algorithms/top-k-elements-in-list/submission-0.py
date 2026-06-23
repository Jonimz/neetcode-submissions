class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1

        # Step 2: find the top k frequent elements
        result = []

        for _ in range(k):
            max_num = None
            max_freq = 0

            for num in count:
                if count[num] > max_freq:
                    max_freq = count[num]
                    max_num = num

            result.append(max_num)
            count[max_num] = 0   # mark as used so we don’t pick it again

        return result
  