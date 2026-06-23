class Solution:
    def twoSum(self, nums, target):
        prevMap={} #create a map to store the val in
        for i, n in enumerate(nums): #loop through the map
            diff = target-n # the diffrence of would be the target - the number
            if diff in prevMap: #if that diffrence is in the map
                return[prevMap[diff], i] #return the diffrence
            prevMap[n]=i