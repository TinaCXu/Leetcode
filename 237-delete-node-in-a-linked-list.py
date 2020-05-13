#   x->x->1->2->3->4
#   x->x->2->3->4
#   x->x->2->2->3->4
#      p  c  n
#      p  c     n               4
#   p  c  n                5
#   p     c  



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # change the value of head
        cur = node
        Next = cur.next
        cur.val = Next.val
        # change next
        cur.next = Next.next

        #key point  here: I only got the node to be deleted, not the head
        #it is impossible to do prev.next = cur.next to delete this node.
        
        # I will make the value of each node equals to the next node's value.
        # 4 -> 5 -> 1 -> 9 -> None
        #      |    |    
        # 4 -> 1 -> 9 -> None
        cur = node
        while cur != None:
            if cur.next != None:
                cur.val = cur.next.val
                if  cur.next.next == None:
                    # if it is the last but two node, it will be the last node.
                    cur.next = None
            cur = cur.next
        return