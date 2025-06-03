import unittest
from functools import cache
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(remaining: int) -> float:
            if remaining == 0:
                return 0
            return min(
                (1 + dp(remaining - coin) for coin in coins if coin <= remaining),
                default=inf,
            )

        return int(res) if (res := dp(amount)) < inf else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        coins = [1, 2, 5]
        amount = 11
        expected = 3
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)

    def test_example_2(self):
        coins = [2]
        amount = 3
        expected = -1
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)

    def test_example_3(self):
        coins = [1]
        amount = 0
        expected = 0
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)

    def test_case_1(self):
        coins = [186, 419, 83, 408]
        amount = 6249
        expected = 20
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)

    def test_single_coin_exact_match(self):
        coins = [5]
        amount = 5
        expected = 1
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)

    def test_multiple_same_coin(self):
        coins = [1, 3, 4]
        amount = 6
        expected = 2
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)

    def test_impossible_amount(self):
        coins = [3, 5]
        amount = 1
        expected = -1
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)

    def test_large_amount(self):
        coins = [1, 5, 10, 25]
        amount = 30
        expected = 2
        result = self.solution.coinChange(coins, amount)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
