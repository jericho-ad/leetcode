class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Naive implementation: using nested for loop
        # Time complexity: O(n^2)
        
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return (i, j)
        """
                
        # Hashtable implementation
        # Time complexity: O(n)
        
        table = {}
        for count, value in enumerate(nums):
            diff = target - value
            if diff in table:
                return [table[diff], count]
            table.update({value:count})
