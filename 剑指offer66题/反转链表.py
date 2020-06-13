

'''
题目：
输入一个链表，反转链表后，输出新链表的表头
'''

'''
思路：使用三个指针，分别为leftPointer,midPointer,rightPointer,
这三个指针可以确保所有的节点数据不被丢失

'''

class Solution:
    def reverseList(self,pHead):
        # 1.将现有的头换成尾，尾部的next为空
        # 2.将从第二个node开始，循环将next指向前一个
        # 3.需要一直有一个指针指向还没有翻转的链表的头部
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead

        leftPointer = pHead
        midPointer = pHead.next
        rightPointer = midPointer.next
        leftPointer.next = None

        while rightPointer != None:
            midPointer.next = leftPointer
            leftPointer = midPointer
            midPointer = rightPointer
            rightPointer = rightPointer.next

        midPointer.next = leftPointer
        return midPointer