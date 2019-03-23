"""
题目描述：
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
最长路径的长度为树的深度。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        depth = 0
        if pRoot:
            depth += 1
            left_depth = self.TreeDepth(pRoot.left)
            right_depth = self.TreeDepth(pRoot.right)
            depth += max(left_depth, right_depth)
        return depth


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
print(Solution().TreeDepth(node1))
