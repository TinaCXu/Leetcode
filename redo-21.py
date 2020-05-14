# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        next_to_add = None
        head = None
        if cur1 == None:
            return cur2
        if cur2 == None:
            return cur1

        while cur1 != None and cur2 !=None:
            print(cu1.val,cul2.val)
            if cur1.val <= cur2.val:
                next_to_add = cur1
                cur1 = cur1.next
            else:
                next_to_add = cur2
                cur2 = cur2.next
            print(next_to_add)
            next_to_add.next = None
            print(head)
            if head == None:
                head = next_to_add
                last = head
            else:
                last.next = next_to_add
                last = last.next
            print(last)
        
        if cur1 == None:
            last.next = cur2
        if cur2 == None:
            last.next = cur1

        return head


