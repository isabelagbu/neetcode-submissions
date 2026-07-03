class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set
        # populate set using loop 
        # if already in set, true
        # else add to set
        # loop ends, false

        #space: O(n) - no duplicates so whole nums in run through
        #time: O(n) - loop through entire nums, worst case

        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False