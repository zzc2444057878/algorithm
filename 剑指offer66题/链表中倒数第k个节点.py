

'''
题目：
输入一个链表，输出该链表中倒数第k个节点
'''

'''
思路：定义两个指针，两个指针间隔k个长度，然后从前往后移动，
直到前一个指针走到最后一个元素，那么后一个指针指向的就是倒数第k个节点
'''

class Solution:
    def find_k(self,head,k):
        # 如果k大于链表长度，直接返回None
        first_point = head
        second_point = head

        for i in range(k):
            if first_point == None:
                return None
            first_point = first_point.next

        while first_point != None:
            first_point = first_point.next
            second_point = second_point.next

        return second_point