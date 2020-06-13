

'''
题目：
输入一个链表，按链表值从尾到头返回一个ArrayList
'''

'''
思路：
新建一个列表，遍历原有链表，将每一个值插入到新列表的第一个位置
'''

class List_node:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def print_list(self,list_node):
        ret = []
        pTmp = list_node

        while pTmp:
            ret.insert(0,pTmp.val)
            pTmp = pTmp.next
        return ret