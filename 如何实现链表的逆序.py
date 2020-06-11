

'''
'''
class LNode:
    def __new__(self,x):
        self.data = x
        self.next = None

    # 方法功能：对单链表进行逆序，输入参数：head，链表头结点

def reverse(head):
    # 判断链表是否为空
    if head == None or head.next == None or head.next.next == None:
        return
    pre = None
    cur = None
    next = None
    # 对链表进行向后遍历
    cur = head.next
    next = cur.next
    cur.next = None
    pre = cur
    cur = next
    # 使当前遍历到的节点cur指向其前驱结点
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = cur.next
        cur = next
    # 链表最后一个节点指向倒数第二个节点
    cur.next = pre
    # 链表的头结点指向原来链表的尾节点
    head.next = cur


if __name__ == '__main__':
    i = 1
    # 链表头结点
    head = LNode('w')
    head.next = None
    tmp = None
    cur = head
    # 构造单链表
    while i < 8:
        tmp = LNode('s')
        tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print('排序前:')
    cur = head.next
    while cur != None:
        print(cur.data)
    print('逆序后：')
    reverse(head)
    cur = head.next
    while cur != None:
        print(cur.data)
        cur = cur.next