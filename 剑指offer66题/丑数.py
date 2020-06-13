

'''
题目:
把只包含质因子2、3和5的数称作丑数(Ugly Number)。例如6,8都是丑数，但14不是，
因为它包含质因子7.习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
'''

'''
思路：
第一种：暴力破解，将一个数字除以2，3,5最后剩下的商为1则该数是丑数，否则不是，
要找出第200个丑数，第200个丑数是16200，得将数字1加到16200，并对从1-16200判断每一个数字是否是丑数
第二种：因为丑数是从小到大进行排列的，大的丑数必然是由小的丑数乘以2或3或5得出来的，
我们需要找到这些丑数，并且找出最小的丑数，添加到后面
'''

class Solution:

    def get_ugly_number_1(self,index):
        if index < 1:
            return 0

        # 死循环，找丑数
        # 判断一个数是不是丑数，先循环除以2，直到不能整除
        # 循环除以3，直到不能整除，循环除以5，直到不能整除
        # 这时候如果剩余的值是1，它就是丑数，反之不是
        count = 0
        def is_ugly_number(num):
            while num % 2 == 0:
                num //= 2
            while num % 3 == 0:
                num //= 3
            while num % 5 == 0:
                num //= 5
            if num == 1:
                return True
            else:
                return False

        num = 1
        while True:
            if is_ugly_number(num):
                count += 1
            if count == index:
                return num
            num += 1

    def get_ugly_number_2(self,index):
        if index < 1:
            return 0

        ugly_list = [1]
        two_pointer = 0
        three_pointer = 0
        five_pointer = 0
        count = 1
        while count != index:
            min_value = min(2*ugly_list[two_pointer],3*ugly_list[three_pointer],5*ugly_list[five_pointer])
            ugly_list.append(min_value)
            count += 1
            if min_value == 2*ugly_list[two_pointer]:
                two_pointer += 1
            if min_value == 3*ugly_list[three_pointer]:
                three_pointer += 1
            if min_value == 5*ugly_list[five_pointer]:
                five_pointer += 1
        return ugly_list[count-1]