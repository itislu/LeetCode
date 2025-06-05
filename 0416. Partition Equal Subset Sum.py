import unittest
from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def subsetSum(s: int, end: int) -> bool:
            if s == 0:
                return True
            if s < 0 or end == 0:
                return False
            return subsetSum(s, end - 1) or subsetSum(s - nums[end - 1], end - 1)

        s = sum(nums)
        return s % 2 == 0 and subsetSum(s // 2, len(nums))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 5, 11, 5]
        expected = True
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [1, 2, 3, 5]
        expected = False
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_case_1(self):
        nums = [3, 3, 6, 8, 16, 16, 16, 18, 20]
        expected = True
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [1]
        expected = False
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_two_equal_elements(self):
        nums = [1, 1]
        expected = True
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_two_unequal_elements(self):
        nums = [1, 2]
        expected = False
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_all_same_elements(self):
        nums = [2, 2, 2, 2]
        expected = True
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_odd_sum(self):
        nums = [1, 2, 3]
        expected = True
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_large_values(self):
        nums = [100, 100]
        expected = True
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_complex_partition(self):
        nums = [1, 2, 5, 10, 20]
        expected = False
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)

    def test_multiple_ways_to_partition(self):
        nums = [3, 3, 3, 4, 5]
        expected = True
        result = self.solution.canPartition(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
