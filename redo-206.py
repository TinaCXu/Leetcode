# Definition for singly-linked list.
# class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#    1->2->3->4->5->NULL
# p  c  n 
# NULL<-1<-2  3->4->5
#       p  c  n
#          p  c  n
# 改变statue一定是current，pcn的链条不能断 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur != None:
            # cur.next = prev
            # prev = cur
            # cur = prev.next
            # 错误原因：没有prev.next，链条已经断掉，一定要先把next记录下来
        
            # record context
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

# _<-1  2->3->4->5  NULL
# p  c  n   

# OLD:
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #initate
        cur = head
        prev = None
        while cur != None:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next
        return prev
a = 3
b = 2
a = a + b
b = (a' + b') - b = a'
a = a' + b' - a' = b'
a = a + b
5 = 3 + 2
b = a - b
3 = 5 - 2
a = a - b 
2 = 5 - 3

a = 2
b = 3
#  <-1  2->3->4->5->NULL
# p  c  n
#    p  c  n
