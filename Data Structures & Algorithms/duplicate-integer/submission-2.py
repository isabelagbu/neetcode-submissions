class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #initialize empty dict
        #loop through nums
        #if num not in dict. add. initialize to 1
        #if num in dict. return true
        #return false when loop ends
    

        my_dict = {}

        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1
            else:
                return True

        return False


        