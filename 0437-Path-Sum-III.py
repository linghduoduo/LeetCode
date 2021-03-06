###Definition for a binary tree node.
###class TreeNode(object):
###    def __init__(self, x):
###        self.val = x
###        self.left = None
###        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        
        res = self.dfs(root, sum)
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res
    
    def dfs(self, root, sum):
        if not root: return 0

        partial = 0
        if root.val == sum:
            partial += 1
        partial += self.dfs(root.left, sum-root.val)
        partial += self.dfs(root.right, sum-root.val)
        return partial

