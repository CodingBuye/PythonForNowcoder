"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def has_subtree(self, root1, root2):
        res = False
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                res = self.does_tree1_has_tree2(root1, root2)
            if res is False:
                res = self.has_subtree(root1.left, root2)
            if res is False:
                res = self.has_subtree(root1.right, root2)
        return res

    def does_tree1_has_tree2(self, root1, root2):
        if root2 is None:
            return True
        if root1 is None:
            return False
        if root1.val != root2.val:
            return False
        return self.does_tree1_has_tree2(root1.left, root2.left) and self.does_tree1_has_tree2(root1.right, root2.right)


if __name__ == '__main__':
    node1 = TreeNode(8)
    node2 = TreeNode(8)
    node3 = TreeNode(7)
    node4 = TreeNode(9)
    node5 = TreeNode(2)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node5.left = node6
    node5.right = node7

    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(2)
    node8.left = node9
    node8.right = node10

    print(Solution().has_subtree(node1, node8))
