"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def print_from_top_to_bottom(self, root):
        if not root:
            return []
        cur_stack = [root]
        res = []
        while cur_stack:
            next_stack = []
            for i in cur_stack:
                if i.left:
                    next_stack.append(i.left)
                if i.right:
                    next_stack.append(i.right)
                res.append(i.val)
            cur_stack = next_stack
        return res


if __name__ == "__main__":
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

    r = Solution().print_from_top_to_bottom(node1)
    print(r)
