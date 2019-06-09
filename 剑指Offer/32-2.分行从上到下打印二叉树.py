"""
题目描述：
从上到下按行打印二叉树，同一层的结点按从左到右的顺序打印，每一层打印到一行
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def print_from_top_to_bottom_by_line(self, root):
        if not root:
            return []
        cur_stack = [root]
        res = []
        while cur_stack:
            next_stack = []
            new_line = []
            for i in cur_stack:
                if i.left:
                    next_stack.append(i.left)
                if i.right:
                    next_stack.append(i.right)
                new_line.append(i.val)
            cur_stack = next_stack
            res.append(new_line)
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

    r = Solution().print_from_top_to_bottom_by_line(node1)
    print(r)
