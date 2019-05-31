"""
题目描述：
如果一个链表中包含环，如何找出环的入口点？

第一步是如何确定一个链表中包含环
第二步是如何找到环的入口
剩下的问题是如何得到环中结点的数量
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def meeting_node(self, head):
        """
        在链表存在环的前提下找到一快一慢指针相遇的结点,

        :param head: 链表的头结点
        :return:
        """
        if head is None:
            return None
        slow = head.next
        if slow is None:
            return None
        fast = slow.next
        while slow is not None and fast is not None:
            if slow == fast:
                return fast

            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
        return None

    def entry_node_of_loop(self, head):
        """
        找到环的入口结点
        :param head: 链表头结点
        :return:
        """
        meet_node = self.meeting_node(head)
        if meet_node is None:
            return None
        loop_nodes = 1
        temp_node = meet_node
        while temp_node.next != meet_node:
            temp_node = temp_node.next
            loop_nodes+=1
        temp_node = head
        for i in range(loop_nodes):
            temp_node = temp_node.next
        temp_node2 = head
        while temp_node2 != temp_node:
            temp_node = temp_node.next
            temp_node2 = temp_node2.next
        return temp_node


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n3
    t = Solution().entry_node_of_loop(n1)
    print(t.val)
