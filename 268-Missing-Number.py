class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tot = n*(n+1)/2

        for i in nums:
        	tot -= i

        return tot