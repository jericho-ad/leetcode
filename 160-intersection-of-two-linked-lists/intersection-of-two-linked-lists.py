# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        """# Implementation using sets 
        # Time complexity: O(n)
        # Space complexity: O(n)
        
        s = set()
        l1 = headA
        l2 = headB
        
        while l1:
            s.add(l1)
            l1 = l1.next
            
        while l2:
            if l2 in s:
                return l2
            else:
                l2 = l2.next
                
        return None"""
    
        # Time complexity: O(n)
        # Space complexity: O(1)
    
        if headA and headB:
            l1 = headA
            l2 = headB
            
            while l1 != l2:
                l1 = l1.next if l1 else headB
                l2 = l2.next if l2 else headA
                
            return l1
        
