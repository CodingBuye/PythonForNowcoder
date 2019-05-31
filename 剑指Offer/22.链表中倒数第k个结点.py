"""
题目描述
输入一个链表，输出该链表中倒数第k个结点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def FindKthToTail(self, head, k):
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         if k > len(arr) or k <= 0:
#             return None
#         return arr[-k]
#
#
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3
#
# node = Solution().FindKthToTail(node1, 1)
# print(node.val)

"""
单向链表的节点只有从前往后的指针
"""


class Solution:
    def find_kth_to_tail(self, head, k):
        if head is None or k < 1:
            return None
        node1 = head
        for i in range(k-1):
            if node1.next:
                node1 = node1.next
            else:
                return None
        node2 = head
        while node1.next:
            node1 = node1.next
            node2 = node2.next
        return node2


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3

    node4 = Solution().find_kth_to_tail(node1, 1)
    print(node4.val)

