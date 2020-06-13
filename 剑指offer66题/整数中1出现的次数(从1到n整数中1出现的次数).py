

'''
题目：
求出1~13的整数中1出现的次数，并计算出100~1300的整数中1出现的次数？为此他
特别数了一下1~13中包含1的数字有1,10,11，12,13因此共出现6次，但是对于后面
问题他就没辙了。ACMer希望你们帮帮他，并把问题更加普遍化，可以很快的求出任意
非负整数区间中1的次数(从1到n中1出现的次数)。
'''

'''
思路：对每一位进行判断，获取它的1的个数，比1大，则该位置上1的个数为
高位上的数字+1乘以低位上的数字+1，等于1，则该位置上的1的个数为高位上的数字+1
乘以低位上的数字+1然后再加上低位上的数字
'''

class Solution:
    def numbers_of_1(self,n):
        # 循环的出口
        hign_value = 1
        preceise = 1
        mid_value = 1
        low_value = 1
        count = 1
        sum_num = 1
        while hign_value != 0:
            hign_value = n // (preceise*10)
            mid_value = (n // preceise) % 10
            low_value = n % preceise
            preceise = preceise * 10

            if mid_value == 0:
                num = (hign_value - 1 + 1) * pow(10,count)
            elif mid_value > 1:
                num = (hign_value + 1) * pow(10,count)
            else:
                num = (hign_value) * pow(10,count) + low_value + 1
            sum_num += num
            count += 1
        return sum_num