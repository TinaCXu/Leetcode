# 6->2->6->3->4->5->6->_
# c  n
# 

#   1->2->6->3->4->5->6->_
#       p c  n
#       p    n 

# 1->2  6  3->4->5->6->_
# p  c  n
# p  c     n
#    p     c  n

#             p  c  n
#             p  c     n
#                       end

# 1->2->6->3->4->5->_
#          p  c  n
#             p  c  n

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#   6->2->6->3->4->5->6->_
# p c  n
#      p  c  n
#      p     c  n


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        cur = head
        while cur != None:
            # delete the node
            if cur.val == val:
                # now i must delete this node
                if prev == None:
                    head = head.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        while cur != None:
            if cur.val == val:
                # now i must delete this node
                if prev == None:
                    head = head.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        # end while, cur == None
        return head





# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         #initiate
#         val=1
#         2 -> 1 -> 3
        
#         while head != None and head.val == val:
#             head = head.next
#         cur = head

#         #loop all the node
#         #change the point of next:cur.next.val == val:
#         while cur != None:
#             #process

#             #move
#             cur = cur.next

#         while cur.next != None:
#             while cur.next.val == val:
#                 cur.next = cur.next.next
#             #jump out while: cur.next.val! == val
#             #change the point of cur: cur.next != None:
#             cur = cur.next
#         #jump out while: cur.next ==  None, return
#         return head