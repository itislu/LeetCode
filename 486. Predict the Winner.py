import unittest
from functools import cache
from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def take(player: int, begin: int, end: int) -> int:
            if begin == end:
                return 0
            if player == 0:
                return max(
                    take(1, begin + 1, end) + nums[begin],
                    take(1, begin, end - 1) + nums[end - 1],
                )
            else:
                return min(
                    take(0, begin + 1, end) - nums[begin],
                    take(0, begin, end - 1) - nums[end - 1],
                )

        return take(0, 0, len(nums)) >= 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 5, 2]
        expected = False
        result = self.solution.predictTheWinner(nums)
        self.assertEqual(result, expected)

    def test_example_2(self):
        nums = [1, 5, 233, 7]
        expected = True
        result = self.solution.predictTheWinner(nums)
        self.assertEqual(result, expected)

    def test_single_element(self):
        nums = [1]
        expected = True
        result = self.solution.predictTheWinner(nums)
        self.assertEqual(result, expected)

    def test_two_elements_equal(self):
        nums = [1, 1]
        expected = True
        result = self.solution.predictTheWinner(nums)
        self.assertEqual(result, expected)

    def test_two_elements_first_larger(self):
        nums = [5, 1]
        expected = True
        result = self.solution.predictTheWinner(nums)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
