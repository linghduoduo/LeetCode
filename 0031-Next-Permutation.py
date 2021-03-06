# class Solution(object):
#     def nextPermutation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         i = len(nums) - 1
#         if i <= 0:
#             return
        
#         targetIndex = 0
#         while i > 1 and nums[i - 1] >= nums[i]:
#             i -= 1
#         if nums[i - 1] < nums[i]:
#             targetIndex = i - 1
        
#         i = len(nums) - 1
#         changeIndex = 0
#         while i > 0 and nums[i] <= nums[targetIndex]:
#             i -= 1
#         if nums[i] > nums[targetIndex]:
#             changeIndex = i
        
#         nums[targetIndex], nums[changeIndex] = nums[changeIndex], nums[targetIndex]
        
#         if targetIndex == changeIndex == 0:
#             nums.reverse()
#         else:
#             nums[targetIndex + 1:] = reversed(nums[targetIndex + 1:])
#         return nums
## 12431
# class Solution(object):
    # def nextPermutation(self, nums):
    #     i = j = len(nums)-1
    #     while i > 0 and nums[i]<=nums[i-1]:
    #         i-=1
    #     i-=1
    #     if i<0:
    #         nums.reverse()
    #         return
        
    #     while j>i and nums[j]<=nums[i]:
    #         j-=1
        
    #     nums[i],nums[j] = nums[j], nums[i]
        
    #     k,l = i+1, len(nums)-1
        
    #     while k<l:
    #         nums[k],nums[l] = nums[l], nums[k]
    #         k+=1
    #         l-=1
    #     return nums


class Solution(object):
    def nextPermutation(self, nums):
        flag = -1
        for i in reversed(range(len(nums)-)):
            if nums[i] < nums[i+1]:
                flag = i
                break

        if flag == -1:
            nums.sort()
        else:
            for i in range(len(nums)-1, flag, -1):
                if nums[i] > nums[flag]:
                    nums[i], nums[flag] = nums[flag], nums[i]
                    nums[flag+1:] = sorted(nums[flag+1:])
                    break
        return nums

# class Solution(object):
#     def nextPermutation(self, nums):
#         i = j = len(nums)-1
#         flag = -1
#         for i in range(len(nums)-2, -1, -1):
#             if nums[i] < nums[i+1]:
#                 flag = i
#                 break

#         if flag<0:
#             nums.reverse()
#             return nums
        
#         while j>i and nums[j]<=nums[i]:
#             j-=1
        
#         nums[i],nums[j] = nums[j], nums[i]
        
#         k,l = i+1, len(nums)-1
        
#         while k<l:
#             nums[k],nums[l] = nums[l], nums[k]
#             k+=1
#             l-=1
        return nums

if __name__ == "__main__":
    nums = [1, 4, 3, 2]
    # nums = [1, 2, 3]
    # nums = [1, 7, 3, 4, 1]
    # nums = [1, 5, 1]
    # nums = [1, 1]
    # nums = [2, 2, 7, 5, 4, 3, 2, 2, 1]
    result = Solution().nextPermutation(nums)
    print(result)
