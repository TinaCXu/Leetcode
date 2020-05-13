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

