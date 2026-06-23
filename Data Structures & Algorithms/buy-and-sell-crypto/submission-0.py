class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit will store the best profit we can make
        max_profit = 0

        # i represents the day we BUY the stock
        for i in range(len(prices)):
            
            # j represents the day we SELL the stock
            # j must be AFTER i because we must buy before selling
            for j in range(i + 1, len(prices)):
                
                # profit if we buy on day i and sell on day j
                profit = prices[j] - prices[i]

                # update max_profit if this profit is better
                if profit > max_profit:
                    max_profit = profit

        # return the best profit found
        # if no profit was possible, max_profit will still be 0
        return max_profit
