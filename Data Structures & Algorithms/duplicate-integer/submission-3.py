class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # dictionary
        #initialize empty dict
        #loop through nums
        #if num not in dict. add. initialize to 1
        #if num in dict. return true
        #return false when loop ends
    
        #my_dict = {}

        #for i in range(len(nums)):
        #    if nums[i] not in my_dict:
        #        my_dict[nums[i]] = 1
        #    else:
        #        return True

        #return False


        # set
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

        


        