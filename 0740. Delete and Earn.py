import unittest
from collections import Counter
from functools import cache
from typing import List


class Solution:
    """
    Use hash table mapping occurences to value.
    Sort by num.
    Work top-down from lowest to highest.

    - Subproblems: DP(i) = max sum of value * occurences for i..L
    - Relation: DP(i) = max{DP(i + 1),
                            v[i] * occurence + DP(i + 1) if v[i] + 1 != v[i + 1],
                            v[i] * occurence + DP(i + 2) if v[i] + 1 == v[i + 1]}
    - Topological Order: decreasing i
    - Base Case: DP(L) = 0
    - Original Problem: DP(0)
    - Time: O(L) + O(U * log(U)) sorting where U is unique elems
    """

    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = sorted(Counter(nums).items())

        @cache
        def dp(i: int) -> int:
            if i >= len(counts):
                return 0
            num = counts[i][0]
            occ = counts[i][1]
            next_i = i + (1 if i + 1 == len(counts) or num + 1 != counts[i + 1][0]
                          else 2)
            return max(dp(i + 1), num * occ + dp(next_i))

        return dp(0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 4, 2]
        expected = 6
        result = self.solution.deleteAndEarn(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [2, 2, 3, 3, 3, 4]
        expected = 9
        result = self.solution.deleteAndEarn(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [1]
        expected = 1
        result = self.solution.deleteAndEarn(nums)
        self.assertEqual(result, expected)

    def test_all_same_elements(self):
        nums = [2, 2, 2, 2]
        expected = 8
        result = self.solution.deleteAndEarn(nums)
        self.assertEqual(result, expected)

    def test_empty_array(self):
        nums = []
        expected = 0
        result = self.solution.deleteAndEarn(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
