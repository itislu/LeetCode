import unittest
from functools import cache
from typing import List, Tuple


class Solution:
    # The sorting steps are crucial for performance
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False

        # Try large numbers first for better pruning
        nums.sort(reverse=True)

        @cache
        def dp(i: int, parts: Tuple[int]) -> bool:
            all_zeros = True
            for part in parts:
                if part < 0:
                    return False
                if part > 0:
                    all_zeros = False
                    break
            if all_zeros:
                return True

            if i == len(nums):
                return False

            return any(
                dp(
                    i + 1,
                    tuple(
                        # Sort for better function call caching
                        sorted(parts[:p] + tuple([parts[p] - nums[i]]) + parts[p + 1 :])
                    ),
                )
                for p in range(len(parts))
            )

        t = s // k
        return dp(0, tuple(t for _ in range(k)))


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

    def test_case_1(self):
        nums = [2, 2, 2, 2, 3, 4, 5]
        k = 4
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

    def test_timeout_1(self):
        nums = [10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8]
        k = 11
        expected = False
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)

    def test_timeout_2(self):
        nums = [18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037]
        k = 4
        expected = True
        result = self.solution.canPartitionKSubsets(nums, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
