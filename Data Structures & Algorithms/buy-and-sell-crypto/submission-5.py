class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size_prices = len(prices)
        profits = []

        if size_prices == 0:
            return 0

        for i in range(size_prices - 1):
            for j in range(i + 1, size_prices):
                profits.append(prices[j] - prices[i])

        if len(profits) == 0:
            return 0

        if max(profits) < 0:
            return 0

        return max(profits)
