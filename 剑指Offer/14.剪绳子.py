"""
题目描述：
给你一根长度为n的绳子，请把绳子剪成m段(m、n都是整数，并且n>1,m>1).
每段绳子的长度记为k[0],k[1],...,k[m],
求k[0]×k[1]×...×k[m]乘积最大是多少？
"""


class Solution:

    def max_product_after_cutting_solution1(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        products = [0, 1, 2, 3]

        for i in range(4, length+1):
            max_val = 0
            for j in range(1, i//2 + 1):
                product = products[j] * products[i-j]
                if max_val < product:
                    max_val = product
            products.append(max_val)
        return products[length]

    # 贪婪算法
    def max_product_after_cutting_solution2(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2

        time_of_3 = length // 3
        if length - time_of_3*3 == 1:
            time_of_3 -= 1
        time_of_2 = (length-time_of_3*3) // 2
        return pow(3, time_of_3) * pow(2, time_of_2)


if __name__ == '__main__':
    s = Solution()
    print(s.max_product_after_cutting_solution1(5))
    print(s.max_product_after_cutting_solution2(8))
