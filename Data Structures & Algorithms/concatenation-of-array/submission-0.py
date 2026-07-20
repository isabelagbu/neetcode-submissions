class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # create ans array
        # loop through nums twice
            # concatinating curr to my ans

        # for i in range(len(nums)):
        #     ans.append(nums[i])

        # for j in range(len(nums)):
        #     ans.append(nums[j])

        ans = [0] * (2 * len(nums))

        pointer1 = 0
        pointer2 = len(nums)

        for i in range(len(nums)):
            ans[pointer1] = nums[pointer1]
            ans[pointer2] = nums[pointer1]

            pointer1 += 1
            pointer2 += 1

        return ans

        