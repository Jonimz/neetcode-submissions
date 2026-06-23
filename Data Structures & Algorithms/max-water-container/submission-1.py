class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #use two pointers 
        l = 0
        r = len(heights) - 1
        total = 0

        while l < r:
            area = ( r - l) * min(heights[l], heights[r])
            total = max(total, area)

            if heights[l] < heights[r]:
                l+=1
            else:
                    r-=1
        return total


        




