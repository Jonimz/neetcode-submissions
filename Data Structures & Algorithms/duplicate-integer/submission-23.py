class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # x = 0
        # y= x+1
        # while (x <= len(nums)-2):
        #     if nums[x] == nums[y]:
        #         return True
        #     x+=1
        #     y = x + 1
        # return False


        nums.sort()
        x= 1
        y = x-1
        while (x < len(nums)):
            if nums[x] == nums[y]:
               return True
            x+=1
            y= x-1
        return False

        

        