# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #loop the ListNode, transfer to List
        cur = head
        List = []
        while cur != None:
            val = cur.val
            List.append(val)
            cur = cur.next
        # get the length of List, determin the middle_point
        length = len(List)
        for idx in range(length):
            if List[idx] != List[length-1-idx]:
                return False
        return False
