

'''
题目：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数字[1,2,3,2,2,2,5,4,2]。由于数字2在数组
中出现了5次，超过数组长度的一半，因此输出2，如果不存在则输出0
'''

'''
思路1：
时间复杂度O(n),空间复杂度O(n)
使用字典进行计数，记录出不同的数字出现的次数,如果该字数次数超过
一半，就返回该数字
思路2：
时间复杂度O(n)，空间复杂度O(1)
只需要使用一个变量即可记录出超过一半数字的次数。如果该数组中有超过一半
的数字，那么该数字与任意其他数字进行抵消，最后该数字依然不会抵消完，
至少还会剩下一个
'''

class Solution:
    def more_than_half_1(self,numbers):
        num_count = {}
        num_len = len(num_count)

        for num in numbers:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
            if num_count[num] > num_len >> 1:
                return num
        return 0

    def more_than_half_2(self,numbers):
        last = 0
        last_count = 0

        for num in numbers:
            if last_count == 0:
                last = num
                last_count += 1
            else:
                if num == last:
                    last_count += 1
                else:
                    last_count -= 1

        if last_count == 0:
            return 0
        else:
            # 这种情况是last可能是大于一半的数字
            last_count = 0
            for num in numbers:
                if num == last:
                    last_count += 1
            if last_count > len(numbers) >> 1:
                return last
        return 0
