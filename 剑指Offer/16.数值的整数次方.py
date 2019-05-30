"""
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。
"""


class Solution:

    def Power(self, base, exponent):
        if base == 0.0 and exponent < 0:
            return 0.0
        abs_exponent = exponent
        if exponent < 0:
            abs_exponent = -exponent

        result = self.PowerWithUnsignedPower(base, abs_exponent)

        if exponent < 0:
            result = 1.0 / result
        return result

    def PowerWithUnsignedPower(self, base, exponent):
        res = 1.0
        for i in range(exponent):
            res *= base
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.Power(0.1, -2)
    print(res)
