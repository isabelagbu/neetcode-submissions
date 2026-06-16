class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create hashmap seen
        # loop through nums
            # calculate compliment. compliment = target - current
            # is cimpliment in seen?
                # yes? return index of compliment and current
                # no? add current. keep looping

        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment],i]
            else:
                seen[nums[i]] = i
        