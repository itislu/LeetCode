import unittest
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        amount = 5
        coins = [1, 2, 5]
        expected = 4
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)

    def test_example_2(self):
        amount = 3
        coins = [2]
        expected = 0
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)

    def test_example_3(self):
        amount = 10
        coins = [10]
        expected = 1
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)

    def test_zero_amount(self):
        amount = 0
        coins = [1, 2, 5]
        expected = 1
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)

    def test_multiple_ways(self):
        amount = 4
        coins = [1, 2]
        expected = 3
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)

    def test_impossible_combination(self):
        amount = 7
        coins = [2, 4]
        expected = 0
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)

    def test_timeout_1(self):
        amount = 4681
        coins = [n for n in range(2, 300 * 2 + 1, 2)]
        expected = 0
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)

    def test_timeout_2(self):
        amount = 180
        coins = [n for n in range(2, 300 * 2 + 1, 2)]
        expected = 56634173
        result = self.solution.change(amount, coins)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
