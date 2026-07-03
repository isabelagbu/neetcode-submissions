class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # loop through prices. find min.
        # loop through again. compute profit until best

        minprice = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            
            profit = prices[i] - minprice
            if profit > maxprofit:
                maxprofit = profit

        return maxprofit