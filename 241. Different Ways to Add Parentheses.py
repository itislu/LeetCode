import operator
import re
import unittest
from functools import cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops, nums = self.parse(expression)

        @cache
        def compute(begin: int, end: int) -> List[int]:
            if end - begin == 1:
                return [nums[begin]]
            results = []
            for i in range(begin, end - 1):
                left = compute(begin, i + 1)
                right = compute(i + 1, end)
                results += [ops[i](l, r) for l in left for r in right]
            return results

        return compute(0, len(nums))

    @staticmethod
    def parse(expression: str) -> tuple[List, List[int]]:
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }
        ops, nums = [], []
        for token in re.findall(r"\d+|[+\-*]", expression):
            if op := operators.get(token):
                ops.append(op)
            else:
                nums.append(int(token))
        return (ops, nums)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        expression = "2-1-1"
        expected = [0, 2]
        result = self.solution.diffWaysToCompute(expression)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        expression = "2*3-4*5"
        expected = [-34, -14, -10, -10, 10]
        result = self.solution.diffWaysToCompute(expression)
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_number(self):
        expression = "5"
        expected = [5]
        result = self.solution.diffWaysToCompute(expression)
        self.assertEqual(result, expected)

    def test_simple_addition(self):
        expression = "1+2"
        expected = [3]
        result = self.solution.diffWaysToCompute(expression)
        self.assertEqual(result, expected)

    def test_simple_multiplication(self):
        expression = "2*3"
        expected = [6]
        result = self.solution.diffWaysToCompute(expression)
        self.assertEqual(result, expected)

    def test_three_numbers_addition(self):
        expression = "1+2+3"
        expected = [6, 6]
        result = self.solution.diffWaysToCompute(expression)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
