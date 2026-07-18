class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create map
        # loop thorugh nums. comp = target - curr. num : index
            # is comp in map. return
            # no? [comp,index]
        
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                if i < seen[comp]:
                    return [i,seen[comp]]
                else:
                    return [seen[comp],i]
            else:
                seen[nums[i]] = i