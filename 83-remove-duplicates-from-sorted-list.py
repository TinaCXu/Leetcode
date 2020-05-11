# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(0, None)
node2 = ListNode(1, None)
node3 = ListNode(2, None)
node4 = ListNode(3, None)
node3.next = node4
node2.next = node3
node1.next = node2

# random access time complexity is O(1)
# insert  one element  at position 1, insert time comlexity is O(n)
#node1 -> node2 -> node3
cur = node1

cnt = 0
while cur != None:
    cnt += 1
    last = cur
    cur = cur.next #cur = node2
    if cnt == 2:
        last.next = cur.next


print(cnt)

# random access time complexity is O(1)
# insert  one element  at position 1, insert time comlexity is O(n)

# 0 -> 1 -> 2

# Input: 1->1->2->3->3
# Output: 1->2->3

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        #loop:
        while cur != None:
            # judge if it is a duplicate:
            while cur.next != None and cur.val == cur.next.val:
                #rm dup
                cur.next = cur.next.next
            cur = cur.next
        return head
