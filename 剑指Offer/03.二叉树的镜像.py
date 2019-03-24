"""
题目描述
操作给定的二叉树，将其变换为源二叉树的镜像。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, root):
        if root:
            if root.left:
                if root.right:
                    root.left, root.right = root.right, root.left
                else:
                    root.right = root.left
                    root.left = None
            else:
                if root.right:
                    root.left = root.right
                    root.right = None
            self.Mirror(root.left)
            self.Mirror(root.right)
        return root


node1 = TreeNode(8)
node2 = TreeNode(6)
node3 = TreeNode(10)
node4 = TreeNode(5)
node5 = TreeNode(7)
node6 = TreeNode(9)
node7 = TreeNode(11)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node = Solution().Mirror(node1)
print(node.left.val)
print(node.right.val)
