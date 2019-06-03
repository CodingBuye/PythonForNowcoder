"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def merge(self, head1, head2):
        if head1 is None:
            return head2
        elif head2 is None:
            return head1

        if head1.val < head2.val:
            merge_head = head1
            merge_head.next = self.merge(head1.next,head2)
        else:
            merge_head = head2
            merge_head.next = self.merge(head1, head2.next)
        return merge_head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(5)
    node1.next = node2

    node3 = ListNode(3)
    node4 = ListNode(4)
    node3.next = node4
    new_head = Solution().merge(node1, node3)
    while new_head is not None:
        print(new_head.val)
        new_head = new_head.next
