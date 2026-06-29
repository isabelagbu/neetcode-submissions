class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create set
        # loop nums
            # if curr in set. True, dupliccates.
            # esle. add to set.
        # False. no duplicates.

        seenNums = set()
        for i in nums:
            if i in seenNums:
                return True
            else:
                seenNums.add(i)
        return False 