from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Key Intuition:
        - Two Pointers (left / right): left tracks lowest price, right tracks highest price 
        - If right encounters a lower than left, move left to that value

        Edge Cases (Functional): 
        - What happens if there are duplicate prices? 
        - What happens if there are multiple price differences with the same? 
        - Can there be negative inputs? 
        '''
        if len(prices) == 1: return 0       # can't sell over one day 

        left, right = 0, 1 
        max_profit = 0
    
        while right < len(prices):      # [1, 5] n = 6
            max_profit = max(max_profit, prices[right] - prices[left])
            if prices[right] < prices[left]:
                left = right 
            right += 1
            # print(f"l: {left}, r: {right}, max profit: {max_profit}")
        return max_profit

prices = [1]
# output = 5
print(Solution().maxProfit(prices))
