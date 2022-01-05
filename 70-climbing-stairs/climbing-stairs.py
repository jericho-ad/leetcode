class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Recursive solution: does not pass due to time limit
        # Time complexity: O(2^n)
        
        """if n == 1:
            return 1
        elif n == 2: 
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)"""
        
        # Iterative solution:
        # Time complexity: O(n)
        
        a = b = 1
        for i in range(n):
            temp = b
            b = a + b
            a = temp
            
        return a
