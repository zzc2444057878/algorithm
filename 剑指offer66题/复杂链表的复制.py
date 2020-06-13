

'''
题目：
输入一个复杂链表，(每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针指向任意一个节点)，返回结果为复制后复杂链表的head。
(注意：输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空)
'''

'''
思路：
将原先的链表，比如[1,2,3,4]，在其每一个节点之后添加一个相同的节点，
比如新链表变为了[1,1,2,2,3,3,4,4]，然后1.random指向的节点就与
1.random.next指向的节点一样，这个指向的节点的val值一样，这样就相当于
完成了复制，然后再将这个链表断开，变成两个完全一样的链表。
如何断开？
将链表[1,1,2,2,3,3,4,4]中的第一个节点1.next = 1.next.next，直接
指向值为2节点，当然这个过程会将第二个1节点丢失，所以在开始我们创建指针，
保证节点不会丢失
'''

class RandomListNode:
    def __init__(self,x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def clone(self,pHead):
        # 复制一个一样的节点node，并且添加在之前链表的每一个node后面
        if pHead == None:
            return None

        pTemp = pHead
        while pTemp:
            node = RandomListNode(pTemp.label)
            node.next = pTemp.next
            pTemp.next = node
            pTemp = node.next

        # 实现新建node的random的指向
        pTemp = pHead
        while pTemp:
            pTemp.next.random = pTemp.random.next
            pTemp = pTemp.next.next

        # 断开原来的node和新的node之间的连接
        pTemp = pHead
        newHead = pHead.next
        pNewTemp = pHead.next
        while pTemp:
            pTemp.next = pTemp.next.next
            if pNewTemp.next:
                pNewTemp.next = pNewTemp.next.next
                pNewTemp = pNewTemp.next
            pTemp = pTemp.next
        return newHead