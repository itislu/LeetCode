import random
import unittest
from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dp(begin: int, end: int, l_bound: int, r_bound: int) -> int:
            if begin == end:
                return 0
            return max(
                dp(begin, i, l_bound, nums[i])
                + l_bound * nums[i] * r_bound
                + dp(i + 1, end, nums[i], r_bound)
                for i in range(begin, end)
            )

        return dp(0, len(nums), 1, 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 1, 5, 8]
        expected = 167
        result = self.solution.maxCoins(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [1, 5]
        expected = 10
        result = self.solution.maxCoins(nums)
        self.assertEqual(result, expected)

    def test_single_balloon(self):
        nums = [5]
        expected = 5
        result = self.solution.maxCoins(nums)
        self.assertEqual(result, expected)

    def test_three_balloons(self):
        nums = [3, 1, 5]
        expected = 35
        result = self.solution.maxCoins(nums)
        self.assertEqual(result, expected)

    def test_all_zeros(self):
        nums = [0, 0, 0]
        expected = 0
        result = self.solution.maxCoins(nums)
        self.assertEqual(result, expected)

    def test_with_zeros(self):
        nums = [2, 0, 3]
        expected = 9
        result = self.solution.maxCoins(nums)
        self.assertEqual(result, expected)

    def test_timeout(self):
        random.seed(42)
        nums = [random.randint(0, 100) for _ in range(300)]
        expected = 107825396
        result = self.solution.maxCoins(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
