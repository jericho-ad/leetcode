class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # XOR solution with O(n) runtime complexity and O(1) space complexity
        
        ans = 0
        
        for i in nums:
            ans ^= i
            
            
        return ans
