"""
题目描述
定义栈的数据结构，
请在该类型中实现一个能够得到栈中所含最小元素的min函数
（时间复杂度应为O（1））。
"""


class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []  # 辅助栈，保证最后一个元素是栈中的最小值

    def push(self, node):
        self.stack1.append(node)

        # 获取最小值
        minest = self.min()
        if not minest:
            self.stack2.append(node)
        else:
            if node < minest:
                self.stack2.append(node)
            else:
                self.stack2.append(minest)

    def pop(self):
        if self.stack1:
            self.stack2.pop()
            return self.stack1.pop()

    def top(self):
        if self.stack1:
            return self.stack1[-1]

    def min(self):
        if self.stack2:
            return self.stack2[-1]
