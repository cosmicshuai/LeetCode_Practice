"""
You are given a 0-indexed 2D integer array transactions, where transactions[i] = [costi, cashbacki].

The array describes transactions, where each transaction must be completed exactly once in some order. At any given moment, you have a certain amount of money. In order to complete transaction i, money >= costi must hold true. After performing a transaction, money becomes money - costi + cashbacki.

Return the minimum amount of money required before any transaction so that all of the transactions can be completed regardless of the order of the transactions.
"""

"""
Thinking process:
for net loss transcation, the hardest step is the one with largest cashback,
for net gain transaction, the hardest step is the one with largest cost,
so we need to compare those two values, max(max_net_loss_cashback, max_net_gain_cost) + total_net_loss



"""


from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        ans = 0
        maxGain = 0
        maxcb =0
        for cost, cb in transactions:
            if cost > cb:
                ans += (cost - cb)
                maxcb = max(maxcb, cb)
            else:
                maxGain = max(maxGain, cost)
        return ans + max(maxcb, maxGain)