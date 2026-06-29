class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create seenDict
        seenDict = {}

        #loop. target - curr. ans in dict? return. no? keep going
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seenDict:
                return [seenDict[comp],i] if seenDict[comp] < i else [i,seenDict[comp]] 
            else:
                seenDict[nums[i]] = i


        