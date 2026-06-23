class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        # initialize our results array 
        res = []


        # sort through our numbers 
        nums.sort()

        # have our for loop go through our indexes and number
        for i, n in enumerate(nums):
            # we have found a duplicate 
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            l, r = i + 1, len(nums) - 1


            while l < r:
                total = n + nums[l] + nums[r]

                if total < 0:
                    l += 1 


                elif  total > 0:
                    r -= 1 

                else:
                    res.append([n, nums[l], nums[r]])


                    l += 1 
                    r -= 1 

                    # what is this code doing right here? 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1  

        return res

                



        