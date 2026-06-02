class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        # loop through nums
            # compliment. target - current
            # check if comp in list
                # yes? return index compliment and current 


        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in nums and i != nums.index(compliment):
                return sorted([i,nums.index(compliment)])
                 

        