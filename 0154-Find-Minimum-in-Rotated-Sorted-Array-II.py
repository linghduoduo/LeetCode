class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if nums is None:
        #     return
        # if len(nums) == 1:
        #     return nums[0]
        
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i - 1]:
        #         return nums[i]
        # return nums[0]
        left, right = 0, len(nums)-1

        return self.findmin(nums, left, right)

    def findmin(self, l, r):
        if l+1>=r:
            return min(nums[l], nums[r])

        if nums[l]<nums[r]:
            return nums[l]

        mid = left + (right-lft)//2

        return min(findmin(nums, l, m-1), findmin(nums, m, r))
    
