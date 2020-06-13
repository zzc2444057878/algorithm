

'''
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

'''
思路：
1.空间换时间：新建一个列表，将整数数组进行两次循环，第一次找出所有的奇数
并将奇数添加到前面，第二次找到左右的偶数将偶数添加到后面

2.时间换空间：类似与冒泡排序，如果偶数在奇数前面，则将这两个进行交换，
每次将奇数往前交换，这样就可以将奇数位于偶数之前了
'''

class Solution:
    # 时间换空间
    def reOrderArray(self,array):
        n = len(array)
        for i in range(n-1):
            for j in range(n-i-1):
                if array[j] % 2 == 0 and array[j+1] == 1:
                    array[j],array[j+1] = array[j+1],array[j]
        return array

    # 时间换空间
    def reOrderArray_2(self,array):
        array2 = []
        for i in array:
            if i % 2 == 1:
                array2.append(i)
        for j in array:
            if j % 2 == 0:
                array2.append(i)
        return array2