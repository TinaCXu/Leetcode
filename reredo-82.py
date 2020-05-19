#    1 ->2 ->3 ->3 ->3 -> 4-> 4-> 5
#    p   c   n
#        p                n
#        p                c       n 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        prev = None

        while cur != None:
            nxt = cur.next
            if nxt != None and nxt.val == cur.val:
                #i am in delete mode
                while nxt != None and nxt.val == cur.val:
                    nxt = nxt.next
                #jump out while:nxt == None or cur.val != nxt.val
                #！！！！！
                if prev == None:
                    #delete head
                    head = nxt
                else:
                    prev.next = nxt
                cur = nxt
            else:
                #no delete
                prev = cur
                cur = cur.next
        return head