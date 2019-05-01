"""
题目描述
用两个队列来实现一个栈，完成栈的Push和Pop操作。
栈中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        self.queue1.append(node)

    def pop(self):
        if self.queue2:
            return self.queue2.pop()
        else:
            if self.queue1:
                while self.queue1:
                    self.queue2.insert(0, self.queue1.pop())
                return self.queue2.pop(0)
            else:
                return None


if __name__ == '__main__':
    s = Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    print(s.queue1)
    print(s.queue2)
