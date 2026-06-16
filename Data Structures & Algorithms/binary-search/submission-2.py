class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize left pointer to index 0
        # initialize right to last element index
        # find mid = (left + right)/2
        # target == mid? return mid index
        # target < mid? search left. repeat process
        # target > mid? search right. repeat process
        # if left > right. return -1

        if len(nums) == 1 and nums[0] != target:
            return -1

        left = 0
        right = len(nums) - 1

        for i in range(len(nums)):
            if left > right:
                return -1
            else:
                mid_index = (left + right)//2
                if target == nums[mid_index]:
                    return mid_index
                elif target < nums[mid_index]:
                    right = mid_index - 1
                elif target > nums[mid_index]:
                    left = mid_index + 1


