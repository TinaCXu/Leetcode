class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # initiate
        prev = None
        cur = head
        # loop
        while cur != None:
            nxt = cur.next
            # determine the left point of duplicate list
            if nxt != None and cur.val == nxt.val:
                # determine the right point of duplicate list
                while nxt != None and cur.val == nxt.val:
                    nxt = nxt.next
                # jump out while: nxt == None or cur.val != nxt.val
                if prev == None:
                    head = nxt
                    # cur = nxt
                else:
                    prev.next = nxt
                    # cur = nxt
                cur = nxt
            else:
                prev = cur
                cur = cur.next
        return head
