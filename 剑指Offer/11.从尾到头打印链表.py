"""
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        arr = []
        while listNode:
            arr.insert(0, listNode.val)
            listNode = listNode.next
        return arr


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

print(Solution().printListFromTailToHead(None))
