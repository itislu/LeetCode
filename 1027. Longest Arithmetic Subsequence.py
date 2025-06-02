import unittest
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        differences = {
            nums[j] - nums[i] for i in range(len(nums)) for j in range(i + 1, len(nums))
        }
        max_LAS = 1
        for diff in differences:
            seen = {}
            for num in nums:
                seen[num] = 1 + seen.get(num - diff, 0)
            max_LAS = max(max(seen.values()), max_LAS)

        return max_LAS


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [3, 6, 9, 12]
        expected = 4
        result = self.solution.longestArithSeqLength(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [9, 4, 7, 2, 10]
        expected = 3
        result = self.solution.longestArithSeqLength(nums)
        self.assertEqual(result, expected)

    def test_example_3(self):
        nums = [20, 1, 15, 3, 10, 5, 8]
        expected = 4
        result = self.solution.longestArithSeqLength(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [5]
        expected = 1
        result = self.solution.longestArithSeqLength(nums)
        self.assertEqual(result, expected)

    def test_two_elements(self):
        nums = [1, 2]
        expected = 2
        result = self.solution.longestArithSeqLength(nums)
        self.assertEqual(result, expected)

    def test_all_same(self):
        nums = [2, 2, 2, 2]
        expected = 4
        result = self.solution.longestArithSeqLength(nums)
        self.assertEqual(result, expected)

    def test_no_arithmetic_sequence(self):
        nums = [1, 10, 3, 20]
        expected = 2
        result = self.solution.longestArithSeqLength(nums)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
