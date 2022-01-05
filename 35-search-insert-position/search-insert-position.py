class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # First implementation
        # Runtime complexity: O(n) 
        
        """for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return len(nums)"""
    
        # Second implementation: Bisection search
        # Runtime complexity: O(log n)
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l
                                                                                                                                                                                                                                                                                                    
