class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                a = max(a, min(heights[i], heights[j]) * (j - i))
        return a