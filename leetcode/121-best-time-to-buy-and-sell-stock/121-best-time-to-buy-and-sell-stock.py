class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        min_price = sys.maxsize
        
        for price in prices:
            min_price = min(min_price,price)
            maxProfit = max(maxProfit,price-min_price)
        
                
                
        return maxProfit