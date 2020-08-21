# 111. 二叉树的最小深度
# 给定一个二叉树，找出其最小深度。

# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

# 说明: 叶子节点是指没有子节点的节点

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        minNum = 10**9
        if root.left:
            minNum = min(self.minDepth(root.left), minNum)
        if root.right:
            minNum = min(self.minDepth(root.right), minNum)
        return minNum + 1

