"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        arr = []
        while head:
            arr.append(head)
            head = head.next
        if k > len(arr) or k <= 0:
            return None
        return arr[-k]


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node = Solution().FindKthToTail(node1, 1)
print(node.val)
