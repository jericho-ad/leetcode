class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Very slow algorithm; maybe revisit another time?
        # Time complexity: O(n) 
        # Space complexity: O(1)
        
        binary = format(n, "b")
        
        currmax = 1
        ans = 1
        num = 0
        
        for i in binary:
            if int(i) == 0:
                currmax += 1
            elif int(i) == 1:
                num += 1
                ans = max(ans, currmax)
                currmax = 1
        
        if num == 1: 
            return 0
        return ans
            
