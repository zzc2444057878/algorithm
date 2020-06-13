
# 题目：一只青蛙一次可以跳上1级台阶，
# 也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

'''
假设有n级台阶，青蛙从最后的第n级开始往前跳，可能性为：
	f(n) = f(n-1) + f(n-2) + ... + f(2) + f(1)		---> ①
	青蛙从最后的第n-1级开始往前跳，可能性为：
	f(n-1) = f(n-2) + f(n-3) + ... + f(2) + f(1)	---> ②
	将②式代入①式得：
	f(n) = 2f(n-1)
'''

class Solution:
    # 简单版
    def jumpFloor_1(self,number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        # ret = 1
        a = 1
        for i in range(2,number+1):
            a = 2 * a
        return a

    # 简化版
    def jumpFloor_2(self,number):
        a,b = 1,2
        for i in range(number-1):
            a,b =  b,b*2
        return a

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor_1(6))