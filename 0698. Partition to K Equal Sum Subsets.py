import unittest
from typing import List


class Solution:
    """
    If there is a subset sum of S / k, S / k * 2, ..., S / k * (k - 1),
    then it is possible to make k equal sum subsets.
    """

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False

        dp = [False for _ in range(s + 1)]
        dp[0] = True
        for num in nums:
            for n in range(s, num - 1, -1):
                dp[n] = dp[n - num] or dp[n]

        t = s // k
        return all(dp[t * p] for p in range(1, k + 1))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [1, 2, 3, 4]
        k = 3
        expected = False
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_single_subset(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_k_equals_length(self):
        nums = [1, 1, 1, 1]
        k = 4
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_impossible_sum(self):
        nums = [1, 2, 3, 5]
        k = 2
        expected = False
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [5]
        k = 1
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_equal_elements(self):
        nums = [2, 2, 2, 2, 2, 2]
        k = 3
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_large_element(self):
        nums = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        k = 5
        expected = False
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_perfect_partition(self):
        nums = [1, 1, 2, 2, 3, 3]
        k = 3
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_k_too_large(self):
        nums = [1, 2, 3]
        k = 4
        expected = False
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
