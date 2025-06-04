import unittest
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for _ in range(k)]
        for end in range(1, len(arr) + 1):
            dp[end % k] = max(
                dp[(end - p) % k] + max(arr[end - p : end]) * p
                for p in range(1, k + 1)
                if p <= end
            )

        return dp[len(arr) % k]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        arr = [1, 15, 7, 9, 2, 5, 10]
        k = 3
        expected = 84
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_example_2(self):
        arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
        k = 4
        expected = 83
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_example_3(self):
        arr = [1]
        k = 1
        expected = 1
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_single_element_large_k(self):
        arr = [5]
        k = 10
        expected = 5
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_k_equals_length(self):
        arr = [1, 2, 3, 4, 5]
        k = 5
        expected = 25
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_all_same_elements(self):
        arr = [3, 3, 3, 3]
        k = 2
        expected = 12
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_strictly_increasing(self):
        arr = [1, 2, 3, 4, 5]
        k = 2
        expected = 17
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_strictly_decreasing(self):
        arr = [5, 4, 3, 2, 1]
        k = 3
        expected = 19
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)

    def test_large_values(self):
        arr = [100, 200, 300]
        k = 2
        expected = 700
        result = self.solution.maxSumAfterPartitioning(arr, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
