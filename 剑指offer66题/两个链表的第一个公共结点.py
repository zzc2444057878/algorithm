

'''
题目：
输入两个链表，找出它们的第一个公共结点
'''

'''
思路：
这两个链表的公共结点必为最后的几个结点，不可能出现在中间部分，
但可能出现在起始位置，因为两个链表有可能一样长
当两个链表不一样长的时候，一长一短，我们可以直接遍历两个链表，
当较短的遍历完之后，退出循环，此时长的链表还没遍历完，我们可以找出
较长链表继续遍历，使用计数器统计出长度之差，然后再重新开始，先将
长链表遍历k个长度，接下来两个的长度一样，再对两个进行遍历，找到
他们相等的节点，该节点则为我们要找的结点
'''

class Solution:
    def find_first_node(self,pHead1,pHead2):
        pTemp1 = pHead1
        pTemp2 = pHead2
        while pTemp1 and pTemp2:
            # 可能会出现两个链表相等的情况
            if pTemp1 == pTemp2:
                return pTemp1
            pTemp1 = pTemp1.next
            pTemp2 = pTemp2.next

        # 遍历完之后找出差值k
        if pTemp1:
            k = 0
            while pTemp1:
                pTemp1 = pTemp1.next
                k += 1

            # 先让长的走k步
            pTemp1 = pHead1
            for i in range(k):
                pTemp1 = pTemp1.next

            # 走完之后判断他们是否相等
            while pTemp1 != pTemp2:
                pTemp1 = pTemp1.next
                pTemp2 = pTemp2.next
            return pTemp1

        if pTemp2:
            k = 0
            while pTemp2:
                pTemp2 = pTemp2.next
                k += 1

            # 先让长的走k步
            pTemp2 = pHead2
            for i in range(k):
                pTemp2 = pTemp2.next

            # 走完之后判断他们是否相等
            while pTemp1 != pTemp2:
                pTemp1 = pTemp1.next
                pTemp2 = pTemp2.next
            return pTemp1