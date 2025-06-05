import random
import unittest
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = {}
        for num in arr:
            seen[num] = 1 + seen.get(num - difference, 0)
        return max(seen.values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr = [1, 2, 3, 4]
        difference = 1
        expected = 4
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_example_2(self):
        arr = [1, 3, 5, 7]
        difference = 1
        expected = 1
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_example_3(self):
        arr = [1, 5, 7, 8, 5, 3, 4, 2, 1]
        difference = -2
        expected = 4
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_single_element(self):
        arr = [5]
        difference = 3
        expected = 1
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_no_valid_subsequence(self):
        arr = [1, 2, 3]
        difference = 5
        expected = 1
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_zero_difference(self):
        arr = [4, 4, 4, 4]
        difference = 0
        expected = 4
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)

    def test_timeout(self):
        random.seed(42)
        arr = [random.randint(-(10**4), 10**4) for _ in range(10**5)]
        difference = 5692
        expected = 4
        result = self.solution.longestSubsequence(arr, difference)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
