# Definition for singly-linked list.

#   1 -> 2 -> 3 -> 3 -> 3 -> 4
#        p    c    n
# judge c = n, move
#   1 -> 2 -> 3 -> 3 -> 3 -> 4
#        p    c              n
# p remain , p.next = new c, judge c = n, move
#   1 -> 2 -> 3 -> 3 -> 3 -> 4
#        p              c    n
# p remain, p.next = new c, judge c != n, move
#   1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 5 ->
#                            p    c    n

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur != None:
            # if cur == cur.next:
            #     cur = cur.next
            # else:
            #     prev = cur.next
            #     cur = cur.next.next
            next = cur.next
            if next != None and cur.val == next.val:
                #in this  case I need to delete
                
                #I will move next pointer until it points to another value
                while next != None and next.val == cur.val:
                    next = next.next
                #here, next must be None or a node with another value
                #which means I will delete cur to next
                prev.next = next
                #move
                prev = prev
                cur = next
            else:
                #in this case I will reserve cur
                prev = cur
                cur = next

            # if cur != cur.next:
            #     prev = cur.next
            #     cur = cur.next
            #     prev.next = cur
            # cur = cur.next

        return head

