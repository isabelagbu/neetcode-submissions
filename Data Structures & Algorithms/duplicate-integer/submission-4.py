class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # initialize empty set
        # loop through nums
            # check if num exists in hashset
                # yes? return true - duplicate found
                # no? add to hashset     
        # return false - no duplicate found

        my_set = set()

        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)      
        return False

        


        