# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reverseList(self, head):
        
        # Time complexity: O(n)
        
        prev = None
        curr = head
        
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
            
        return prev
