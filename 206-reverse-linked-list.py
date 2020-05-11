# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        cnt = 0
        # loop
        # 1 -> 2 -> 3 -> 4
        # 
        # ppprev <- pprev <- prev  cur -> next -> ...
        # ppprev <- pprev <- prev <- cur  next -> ...
        # ....... 
        # 
        # 1. reverse:
        #       1. cur.next = prev    ppprev <- pprev <- prev <- cur next
        # 2. maintain prev, cur, next 
        # prev = cur
        # cur = next
        # next = cur.next
        #   <-1 -> 2 -> 3 -> 4
        #  p  c    n
        #  prev = cur
        #     c    n
        #     p    
        #  cur = next
        #          n
        #     p    c
        #   1 -> 2 -> 3 -> 4
        #p  c  n
        #   1 <- 2 <- 3 <- 4  None
        #                  p  c  n
        # ppprev <- pprev <- prev <- cur next -> ...
        prev = None
        while cur != None:
            #record context
            next = cur.next
            #operation
            cur.next = prev
            # move
            prev = cur
            cur = next
        return prev


        while cur != None and cur.next != None: 
            cnt += 1
            last = cur
            cur = cur.next
            Next = cur.next
            cur.next = last
            if cnt == 1:
                last.next = None
        return head
                    
