from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if (prices[i] - prices[i - 1]) > 0:
                max_profit += (prices[i] - prices[i - 1])
        return max_profit


if __name__ == "__main__":
    nums = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(nums))
