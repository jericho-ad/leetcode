class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Kadane's algorithm
        # Time complexity: O(n)
        
        max_ending_here = 0
        max_so_far = -1000000
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            max_ending_here += nums[i]
            
            if max_ending_here < nums[i]:
                max_ending_here = nums[i]
                
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
        
        return max_so_far
