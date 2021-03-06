# class Solution:
#     def jump(self, nums) -> int:
#         n = len(nums)
#         res = 0

#         reach = 0
#         cur = 0
#         i = 0
#         while cur < n - 1:
#             res += 1
#             potential = cur
#             while i <= potential:
#                 cur = max(cur, i + nums[i])
#                 i += 1
#         return res

class Solution:
    def jump(self, nums) -> int:
        if not nums or len(nums) < 2:
            return 0

        res = 0
        cur = 0
        maxreach = 0

        for i in range(len(nums)-1):
            maxreach = max(maxreach, i + nums[i])
            if i == cur:
                res += 1
                cur = maxreach
        return res

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    results = Solution().jump(nums)
    print(results)

