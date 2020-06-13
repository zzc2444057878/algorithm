
# 题目：大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39

class Solution:
    # 时间复杂度O(n)
    def Fibnacci_1(self,n):
        a,b = 0,1
        for i in range(n):
            a,b = b,a+b
        return a

    # 时间复杂度O(2**n)
    def Fibnacci_2(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            num = self.Fibnacci_2(n-1) + self.Fibnacci_2(n-2)
            return num
        return None

if __name__ == '__main__':
    s = Solution()
    print(s.Fibnacci_1(5))