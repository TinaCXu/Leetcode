# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        cur = head
        # get length
        while cur != None:
            #if cur.next != None:
            cnt += 1
            cur = cur.next
        # judge the middle point 
        middle_index = cnt // 2 # 4 // 2 = 2, 5 // 2 = 2
        
        #get index = middle_index
        index = 0
        cur = head
        while cur != None:
            if index == middle_index:
                return cur
            index += 1
            cur = cur.next

