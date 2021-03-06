class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]

        Input: k = 3, n = 7
                Output: [[1,2,4]]
        """
        self.res = []

        for i in range(1, 10):
            self.dfs(k - 1, n - i, i + 1, [i])

        return self.res

    def dfs(self, k, n, idx, path):
        if k == 0 and n == 0:
            self.res.append(path)

        for i in range(idx, 10):
            self.dfs(k - 1, n - i, i + 1, path + [i])
        return

if __name__ == '__main__':
    k=3
    n=7
    result = Solution().combinationSum3(k, n)
    print(result)
    
    k=3
    n=9
    result = Solution().combinationSum3(k, n)
    print(result)

    k=3
    n=15
    result = Solution().combinationSum3(k, n)
    print(result)