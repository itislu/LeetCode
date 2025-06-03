from functools import cache
import unittest


class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 2
        expected = 1
        result = self.solution.fib(n)
        self.assertEqual(result, expected)

    def test_example_2(self):
        n = 3
        expected = 2
        result = self.solution.fib(n)
        self.assertEqual(result, expected)

    def test_example_3(self):
        n = 4
        expected = 3
        result = self.solution.fib(n)
        self.assertEqual(result, expected)

    def test_base_cases(self):
        n = 0
        expected = 0
        result = self.solution.fib(n)
        self.assertEqual(result, expected)

        n = 1
        expected = 1
        result = self.solution.fib(n)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
