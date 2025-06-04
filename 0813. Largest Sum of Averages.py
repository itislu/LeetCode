import unittest
from functools import cache
from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        cur = 0
        prefix_sums = [0] + [(cur := cur + num) for num in nums]

        def avg(begin: int, end: int) -> float:
            if begin == end:
                return 0
            return (prefix_sums[end] - prefix_sums[begin]) / (end - begin)

        @cache
        def dp(end: int, k: int) -> float:
            if k == 1 or end == 0:
                return avg(0, end)
            return max(dp(i, k - 1) + avg(i, end) for i in range(end))

        return dp(len(nums), k)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [9, 1, 2, 3, 9]
        k = 3
        expected = 20.00000
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)

    def test_example_2(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 4
        expected = 20.50000
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)

    def test_single_element(self):
        nums = [5]
        k = 1
        expected = 5.0
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)

    def test_k_equals_length(self):
        nums = [1, 2, 3, 4]
        k = 4
        expected = 10.0
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)

    def test_k_equals_one(self):
        nums = [1, 2, 3, 4, 5]
        k = 1
        expected = 3.0
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)

    def test_all_same_elements(self):
        nums = [3, 3, 3, 3]
        k = 2
        expected = 6.0
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)

    def test_large_values(self):
        nums = [100, 200, 300]
        k = 2
        expected = 450.0
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)

    def test_timeout(self):
        nums = [7958,2136,9787,7340,2560,8919,8055,5309,6477,867,9790,5577,9995,7166,389,3952,7973,3293,206,8560,3312,9053,5035,7231,5058,1420,6243,4420,5047,8150,7024,2000,7914,9097,1023,2938,4946,7236,1501,6189,9048,6559,9952,6533,7963,1049,208,2049,3107,9530]
        k = 33
        expected = 219773.81667
        result = self.solution.largestSumOfAverages(nums, k)
        self.assertAlmostEqual(result, expected, places=5)


if __name__ == "__main__":
    unittest.main()
