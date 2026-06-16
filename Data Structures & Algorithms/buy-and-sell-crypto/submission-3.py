class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # initialize min_price to first index
        # initilize max_profit to 0
        # loop through prices
            # if current < min_price. update.
            # calculate profit = current - min_price
            # if profit > max. update
        # return max_profit

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

        