"""
题目描述：
给定一个没有排序的链表，去掉其重复项，并保留原来的顺序，例如链表1->3->1->5->5->7,
去掉重复项后变为1->3->5->7
"""


class LNode:
    def __init__(self, x):
        self.data = x
        self.next = None


def remove_dup(head):
    """
    ** 方法功能：对带头结点的无序单链表删除重复的节点
    ** 输入参数：head：链表头节点
    """
    if head is None or head.next is None:
        return head
    outer_cur = head.next
    while outer_cur is not None:
        inner_cur = outer_cur.next
        inner_pre = outer_cur
        while inner_cur is not None:
            if inner_cur.data == outer_cur.data:
                inner_pre.next = inner_cur.next
                inner_cur = inner_cur.next
            else:
                inner_pre = inner_cur
                inner_cur = inner_cur.next
        outer_cur = outer_cur.next


if __name__ == '__main__':
    i = 1
    head = LNode(None)
    temp = None
    cur = head
    while i < 7:
        if i % 2 == 0:
            temp = LNode(i+1)
        elif i % 3 == 0:
            temp = LNode(i-2)
        else:
            temp = LNode(i)
        cur.next = temp
        cur = temp
        i += 1
    print("删除重复节点前：")
    c = head.next
    while c is not None:
        print(c.data)
        c = c.next
    remove_dup(head)
    print("删除重复节点后：")
    d = head.next
    while d is not None:
        print(d.data)
        d = d.next
