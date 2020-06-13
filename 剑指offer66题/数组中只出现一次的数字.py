

'''
题目：
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。
请写程序找出这两个只出现一次的数字。
'''

'''
思路：
a^b^c = a^c^b
两个数字相等，异或结果为0，两个数字不等，亦或结果为1，将他们所有的
进行异或，得到的结果是两个出现奇数次的数字进行异或的结果。
再将该结果与数组中所有的数字进行(与)操作，会得到0或者1这样的结果。
将所有结果为0的进行异或，会得到第一个出现奇数次的数字，
将所有结果为1的进行异或，会得到第二个出现奇数次的数字
'''

class Solution:
    def find_number(self,array):
        # 如果两个数字相同，那么这两个数的异或操作等于0
        if len(array) < 2:
            return None
        two_num_xor = None
        for num in array:
            if two_num_xor == None:
                two_num_xor = num
            else:
                two_num_xor = two_num_xor ^ num

        count = 0
        while two_num_xor % 2 == 0:
            two_num_xor = two_num_xor >> 1
            count += 1
        mask = 1 << count

        first_num = None
        second_num = None

        for num in array:
            if mask & num == 0:
                if first_num == None:
                    first_num = num
                else:
                    first_num = first_num ^ num
            else:
                if second_num == None:
                    second_num = num
                else:
                    second_num = second_num ^ num
        return first_num,second_num