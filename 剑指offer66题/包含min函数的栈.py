

'''
题目：
定义栈的数据结构，请在该类型中实现一个能够得到栈中最小元素的min函数
时间复杂度为O(1)
'''

'''
思路：要求时间复杂度为O(1)，那么空间复杂度就可以高点，我们可以新建一个空列表，用来装和原栈几乎相同的数据
怎么装？
当入栈的时候，检查最小值的那个栈的-1个元素与新入栈的元素的大小，如果新入栈的元素比下标为-1元素小，则将这个元素也
添加到最小栈，否则将原来下标为-1的元素复制一个出来添加到最小栈的最后，
最小栈元素的顺序排列是一个非递增的序列，保证最后一个元素必定为当前栈的最小值
'''

class Solution:
    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self,node):
        self.stack.append(node)
        if self.min_value:
            if self.min_value[-1] > node:
                self.min_value.append(node)
            else:
                self.min_value.append(self.min_value[-1])
        else:
            self.min_value.append(node)

    def pop(self):
        if self.stack == []:
            return None
        self.min_value.pop()
        return self.stack.pop()

    def top(self):
        if self.stack == []:
            return None
        return self.stack[-1]

    def min(self):
        if self.min_value == []:
            return None
        return self.min_value[-1]