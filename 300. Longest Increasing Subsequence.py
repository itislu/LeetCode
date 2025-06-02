import unittest
from functools import cache
from typing import List


class Solution:
    """
    - Subproblem: LIS(N[:i]) that ends with N[i]
    - Relation: LIS(N[:i]) = 1 + max{LIS(N[:j]) | 0 < j < i, N[j] < N[i]}
    - Topological Order: increasing i
    - Base Case: LIS([]) = 0
    - Original Problem: max{LIS(N[:i]) | 1 <= i <= N}
    - Time: O(N * N)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def LIS(i: int) -> int:
            if i == 0:
                return 1
            return 1 + max((LIS(j) for j in range(i) if nums[j] < nums[i]), default=0)

        return max((LIS(i) for i in range(len(nums))), default=0)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        expected = 4
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_example_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        expected = 1
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [5]
        expected = 1
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        expected = 5
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        expected = 1
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_timeout(self):
        nums = [i for i in range(2500)]
        expected = 2500
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_lecture_1(self):
        nums = [ord(c) for c in "CARBOHYDRATE"]
        expected = 5
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)

    def test_lecture_2(self):
        nums = [ord(c) for c in "EMPATHY"]
        expected = 5
        result = self.solution.lengthOfLIS(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
