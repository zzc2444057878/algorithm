

'''
题目：
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为
该栈的弹出顺序。假如压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的
压入顺序，序列4,5,3,2,1是该栈序列对应的一个弹出序列，但4,3,5,1,2就不可
能是该压栈序列的弹出序列。(注意：这两个序列的长度是相等的)
'''

'''
思路：
先将两个序列输入，遍历第一个栈，循环一次将第一个栈的元素压入，在压入后与第二个栈的元素进行比较，
判断是否一样，直到不一样为止
'''

class Solution:
    def isPopOrder(self,pushV,popV):
        if pushV == [] or len(pushV) != len(popV):
            return None
        stack = []
        index = 0
        for item in pushV:
            stack.append(item)
            while stack and stack[-1] == popV[index]:
                stack.pop()
                index += 1

        # if stack == []:
        #     return True
        # else:
        #     return False
        return True if stack == [] else False