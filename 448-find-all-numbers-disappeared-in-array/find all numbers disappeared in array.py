class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # First implementation, brute force: 
        # Time limit exceeded
        # Would maybe work with hashmap to lower duplicates?
        
        """res = []

        for i in range(1, len(nums) + 1):
            if i not in nums:
                res.append(i)
                
        return res"""
        
        # Mark as seen by negation
        # Time complexity: O(n)
        # Space complexity: O(1)
        
        res = []

        for i in nums:
            nums[abs(i) - 1] = -abs(nums[abs(i) - 1])
            
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
                
        return res
