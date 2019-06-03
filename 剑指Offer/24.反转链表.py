"""
题目描述
输入一个链表，反转链表后，输出新链表的表头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def ReverseList(self, pHead):
#         if not pHead:
#             return None
#         arr = []
#         while pHead:
#             arr.insert(0, pHead.val)
#             pHead = pHead.next
#         new_head = ListNode(arr.pop(0))
#         keep_head = new_head
#         for i in arr:
#             keep_head.next = ListNode(i)
#             keep_head = keep_head.next
#         return new_head
#
#
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node1.next = node2
# node2.next = node3
#
#
# new = Solution().ReverseList(node1)
# while new:
#     print(new.val)
#     new = new.next


class Solution:
    def reserve_list(self, head):
        """
        反转后链表的头结点就是原始链表的尾结点，也就是next为None的结点
        :param head: 头结点
        :return:
        """
        reversed_head = None  # 反转后的链表头结点
        pre_node = None       # 当前结点的前一个结点
        cur_node = head       # 当前结点
        while cur_node is not None:
            next_node = cur_node.next
            if next_node is None:
                reversed_head = cur_node

            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        return reversed_head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    res = Solution().reserve_list(node1)
    print(res.val)
