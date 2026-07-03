class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize minprice and maxprofit
        # loop through prices
             # find min price 
             # compute profit for each price using minprice
        # return maxprofit

        minprice = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            
            profit = prices[i] - minprice
            if profit > maxprofit:
                maxprofit = profit

        return maxprofit