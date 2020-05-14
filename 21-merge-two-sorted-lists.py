# l1 :  1-> 2 ->4
#    p1 c1  n1
# l2 :  1-> 3 ->4
#    p2 c2  n2
# l3:   1-> 2 ->4 ->1->3->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        prev1 = None
        cur2 = l2
        # prev2 = None
        # if cur1 ==  None and cur2 == None:
        #     return cur1
        # elif cur1 !== None and cur2 == None:
        #     return cur1

        # if cur2 == None:
        #     return cur1
        if cur1 == None and cur2 != None:
            return cur2
        while cur1 != None:
            Next1 = cur1.next 
            while cur2 != None:
                Next2 = cur2.next
                if cur1.val <= cur2.val:
                    if Next1.val >= cur2.val:
                        cur1.next = cur2
                        cur2.next = Next1
                    # else: # Next1 < cur2, cur1.next 维持不变,C1变，比较C1与C2直到N1>=C2
                else:
                    # cur1 > cur2
                    if prev1 == None:
                        prev1 = cur2
                        cur2.next = cur1
                    elif prev1.val <= cur2.val:
                        prev1.next = cur2
                        cur2.next = cur1
                    # no else, prev1 must <= cur2
                cur2 = Next2
            #jump out cur2 while: cur2 = None
            cur2 = l2
            cur1 = cur1.next
        #jump out cur1 while: cur1 = None
        return cur1

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        prev = None
        head = None
        cur1 = l1
        cur2 = l2

        p
        1->2->4  
                 c1
        1->3->4
             c2


        l3: 1->1->2->3->4
            h
                        l
        head = None 
        while cur1 != None and cur2 != None:
            next_to_add = None
            if cur1.val <= cur2.val:
                next_to_add = cur1
                cur1 = cur1.next
            else:
                next_to_add = cur2
                cur2 = cur2.next
            next_to_add.next = None
            if head == None:
                head = next_to_add
            else:
                last.next = next_to_add
            last = next_to_add

        if cur1 != None:
            last.next = cur1
        if cur2 !=  None:
            last.next = cur2
        return head

        head = None
        while cur1 != None and cur2 != None:
            # in this case, both lists have nodes, i need to compare
            next_to_add = None
            if cur1.val < cur2.val:
                next_to_add = cur1
                cur1 = cur1.next
            else:
                next_to_add = cur2
                cur2 = cur2.next
            
            copy_node = ListNode(next_to_add.val)

            #now we add next_to_add to l3
            if head == None:
                head = next_to_add
            else:
                prev.next = next_to_add
            prev = next_to_add

        while cur1 != None:
            prev.next = cur1
            prev = cur1
            cur1 = cur1.next
        
        while cur2 != None:
            prev.next = cur2
            prev = cur2
            cur2 = cur2.next
        return head