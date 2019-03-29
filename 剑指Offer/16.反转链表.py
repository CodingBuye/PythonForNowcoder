"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ReverseList(self, pHead):
        if not pHead:
            return None
        arr = []
        while pHead:
            arr.insert(0, pHead.val)
            pHead = pHead.next
        new_head = ListNode(arr.pop(0))
        keep_head = new_head
        for i in arr:
            keep_head.next = ListNode(i)
            keep_head = keep_head.next
        return new_head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3


new = Solution().ReverseList(node1)
while new:
    print(new.val)
    new = new.next
