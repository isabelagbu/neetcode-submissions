class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize left index
        #initialize right index
        #while left < right
        #calculate mid index=(left+right)/2
        #if mid element == target. return mid index
        #if target < mid element. search left
        #if target > mid element. search right
        # return -1 if outside while loop

        left_index = 0
        right_index = len(nums) - 1

        while left_index <= right_index:
            mid_index=(left_index + right_index)//2
            if target == nums[mid_index]:
                return mid_index
            elif target < nums[mid_index]:
                right_index = mid_index - 1
            elif target > nums[mid_index]:
                left_index = mid_index + 1

        return -1
        