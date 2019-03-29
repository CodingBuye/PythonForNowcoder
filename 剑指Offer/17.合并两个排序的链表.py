"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next= None


class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1 and not pHead2:
            return None
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        arr = []
        while pHead1 and pHead2.val:
            if pHead1.val <= pHead2.val:
                arr.append(pHead1.val)
                pHead1 = pHead1.next
            else:
                arr.append(pHead2.val)
                pHead2 = pHead2.next

        while pHead1:
            arr.append(pHead1.val)
            pHead1 = pHead1.next

        while pHead2:
            arr.append(pHead2.val)
            pHead2 = pHead2.next

        new_head = ListNode(arr.pop(0))
        temp_head = new_head
        for i in arr:
            temp_head.next = ListNode(i)
            temp_head = temp_head.next
        return new_head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(3)
node6 = ListNode(4)
node7 = ListNode(5)
node4.next = node5
node5.next = node6
node6.next = node7

a = Solution().Merge(node1, node4)
while a:
    print(a.val)
    a = a.next

