class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = False
        for i in range(len(nums)):
            if found != True:
                num1 = nums[i]
                for j in range(len(nums)):
                    if i != j:
                        num2 = nums[j]
                        if num1 + num2 == target:
                            answer = [i,j]
                            found = True
                            break
        return answer