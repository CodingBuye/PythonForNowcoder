"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。
"""


class Solution:
    def replaceSpace(self, s):
        return s.replace(" ", "%20")

    # def replaceSpace1(self, s):
    #     s_list = []
    #     for i in s:
    #         if i == " ":
    #             s_list.append("%20")
    #         else:
    #             s_list.append(i)
    #     return "".join(s_list)


s = "We Are Happy"
print(Solution().replaceSpace(s))
