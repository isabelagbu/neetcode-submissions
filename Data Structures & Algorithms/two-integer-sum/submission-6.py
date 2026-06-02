class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # creat dict of nums -> index
        # loop through nums agaim. for each, compute ans = target - current.
        # in loop, if ans in dict, return index current and ans

        for i in range(len(nums)):
            ans = target - nums[i]            
            if ans in nums and nums.index(ans) != i:
                if nums.index(ans) < i:
                    return [nums.index(ans),i]
                else:
                    return [i,nums.index(ans)]

        