class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Runtime: O(n)
        
        answer = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            answer = max(answer, profit)
        return answer
