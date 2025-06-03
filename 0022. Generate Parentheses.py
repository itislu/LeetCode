import unittest
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = {"()"}
        for _ in range(1, n):
            dp = {s[:i] + "()" + s[i:] for s in dp for i in range(len(s) + 1)}
        return list(dp)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 3
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_2(self):
        n = 1
        expected = ["()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(result, expected)

    def test_n4(self):
        n = 4
        expected = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
