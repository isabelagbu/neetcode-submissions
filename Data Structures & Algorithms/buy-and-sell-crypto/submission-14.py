class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minprice = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:       # find min price
                minprice = prices[i]

            profit = prices[i] - minprice # calculate current profit

            if profit > maxprofit:   #compare profit to current maxprifot
                maxprofit = profit
        return maxprofit