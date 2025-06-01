import unittest
from functools import cache
from typing import List


class Solution:
    """
    - Subproblems: DP(i) = max sum of money from i..L
    - Relation: DP(i) = max{DP(i + 1), v[i] + DP[i + 2]}
    - Topological Order: decreasing i
    - Base Case: DP(L) = 0
    - Original Problem: DP(0)
    - Time: O(L)
    """

    def rob(self, nums: List[int]) -> int:
        @cache
        def max_money(i: int) -> int:
            if i >= len(nums):
                return 0
            return max(max_money(i + 1), nums[i] + max_money(i + 2))

        return max_money(0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        expected = 4
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [2, 7, 9, 3, 1]
        expected = 12
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_single_house(self):
        nums = [5]
        expected = 5
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_two_houses(self):
        nums = [2, 1]
        expected = 2
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)

    def test_empty_houses(self):
        nums = []
        expected = 0
        result = self.solution.rob(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
