import unittest
from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        # Top-down
        @cache
        def dp(amount: int, max_coin_idx: int) -> int:
            if amount == 0:
                return 1
            return sum(
                dp(amount - coins[i], i)
                for i in reversed(range(max_coin_idx + 1))
                if coins[i] <= amount
            )

        return dp(amount, len(coins) - 1)

        # Bottom-up
        arr = [[0 for _ in coins] for _ in range(amount + 1)]
        for c in range(len(coins)):
            arr[0][c] = 1

        for a in range(1, amount + 1):
            for c in range(len(coins)):
                arr[a][c] = sum(
                    arr[a - coins[i]][i] for i in range(c + 1) if coins[i] <= a
                )

        return arr[amount][-1]


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
