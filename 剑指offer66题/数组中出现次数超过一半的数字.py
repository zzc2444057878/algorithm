

'''
题目：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。由于数字2在数组
中出现了5次，超过数组长度的一半，因此输出2，如果不存在则输出0
'''


class Solution:
    # 这种方法时间复杂度O(n)，空间复杂度O(n)
    # 使用字典进行计数
    def more_than_half_1(self,numbers):
        nums_count = {}
        num_len = len(numbers)

        for num in numbers:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
            if nums_count[num] > (num_len>>1):
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