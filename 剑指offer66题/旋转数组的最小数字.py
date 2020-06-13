

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如：数组{3，4，5，1，2}为{1,2,3,4,5}的一个旋转，该数组的最小数字
为1。NOTE:给出的所有元素都大于0，若数组大小为0，请返回0
'''

'''
思路：二分查找的思想，找出中间数，如果中间数字大于右边数字，则
整个数组的最小数字一定在右半边，反之左边，
如果一个数字的左边一个元素大于它，那么这个数字就是最小数字
'''

class Solution:
    def min_number(self,rotaArray):
        # 数组为空
        if not rotaArray:
            return 0
        left = 0
        right = len(rotaArray) - 1
        while left <= right:
            mid = (left + right) >> 1
            if rotaArray[mid] < rotaArray[mid-1]:
                return rotaArray[mid]
            elif rotaArray[mid] < rotaArray[right]:
                right = mid -1
            else:
                left = mid + 1
        return 0