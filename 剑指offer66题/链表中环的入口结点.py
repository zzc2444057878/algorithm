

'''
题目：
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null
'''

'''
思路：先确认该链表是否包含环，如何确定？
使用快慢指针（快指针：每次走两个长度;慢指针：每次走一个长度），若链表内有环，则快慢指针必定会在环内相遇
如何确定入口结点？
'''

class Solution:
    def enter_node_loop(self,pHead):
        # 没有环
        if pHead == None:
            return None

        fastPointer = pHead
        slowPointer = pHead

        while fastPointer and fastPointer.next:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                break

        if fastPointer == None or fastPointer.next == None:
            return None

        # 如果slow走了l的长度，那么fast走了2l的长度
        # 假设从开始到入口点的长度是s，slow在环里走的长度是d
        # 那么 l = s + d
        # 假设环内slow没走的长度是m，fast走的长度是多少
        # fast走的长度就是 n(m+d)+s+d = 2l
        # 带入 n(m+d)+s+d = 2(s+d)
        # 那么 s 就是从开始到环的长度
        # s = m + (n-1)(m+d)
        # m+d 表示环一圈的长度，走了 n-1 圈

        # 将头结点赋值给fastPointer，此时的slowPointer为快慢指针相遇的地点
        # 满足公式 s = m + (n-1)(m+d)
        fastPointer = pHead

        while fastPointer != slowPointer:
            fastPointer = fastPointer.next
            slowPointer = slowPointer.next

        return fastPointer