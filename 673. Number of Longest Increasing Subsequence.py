import unittest
from collections import namedtuple
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        LIS = namedtuple("LIS", ["length", "count"])
        dp = [LIS(1, 1) for _ in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j].length + 1 > dp[i].length:
                        dp[i] = LIS(dp[j].length + 1, dp[j].count)
                    elif dp[j].length + 1 == dp[i].length:
                        dp[i] = LIS(dp[i].length, dp[i].count + dp[j].count)

        max_length = max(d.length for d in dp)
        return sum(d.count for d in dp if d.length == max_length)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, 5, 4, 7]
        expected = 2
        result = self.solution.findNumberOfLIS(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [2, 2, 2, 2, 2]
        expected = 5
        result = self.solution.findNumberOfLIS(nums)
        self.assertEqual(result, expected)

    def test_case_1(self):
        nums = [1, 2, 4, 3, 5, 4, 7, 2]
        expected = 3
        result = self.solution.findNumberOfLIS(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [5]
        expected = 1
        result = self.solution.findNumberOfLIS(nums)
        self.assertEqual(result, expected)

    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        expected = 1
        result = self.solution.findNumberOfLIS(nums)
        self.assertEqual(result, expected)

    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        expected = 5
        result = self.solution.findNumberOfLIS(nums)
        self.assertEqual(result, expected)

    def test_repeated_elements(self):
        nums = [1, 1, 1, 2, 2, 2]
        expected = 9
        result = self.solution.findNumberOfLIS(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
