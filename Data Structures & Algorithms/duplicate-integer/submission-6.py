class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create dictionary
        # loop through 
            # add to dict if doesnt exist
            # if it does, return true

        # return false 

        seen = set()         #O(n) - time and space
        for i in nums:       
            if i in seen:
                return True
            else: 
                seen.add(i)

        return False
