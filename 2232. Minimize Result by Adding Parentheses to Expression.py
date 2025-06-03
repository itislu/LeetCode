import unittest


class Solution:
    def minimizeResult(self, expression: str) -> str:
        left, right = expression.split("+")
        l_res, r_res = 0, len(right)
        min_res = int(left) + int(right)

        for l in range(len(left)):
            left_mul = int(left[:l] or 1)
            left_add = int(left[l:])
            for r in range(1, len(right) + 1):
                right_add = int(right[:r])
                right_mul = int(right[r:] or 1)

                tmp = left_mul * (left_add + right_add) * right_mul
                if tmp < min_res:
                    min_res = tmp
                    l_res, r_res = l, r

        return (
            left[:l_res]
            + "("
            + left[l_res:]
            + "+"
            + right[:r_res]
            + ")"
            + right[r_res:]
        )


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        expression = "247+38"
        expected = "2(47+38)"
        result = self.solution.minimizeResult(expression)
        self.assertEqual(result, expected)

    def test_example_2(self):
        expression = "12+34"
        expected = "1(2+3)4"
        result = self.solution.minimizeResult(expression)
        self.assertEqual(result, expected)

    def test_example_3(self):
        expression = "999+999"
        expected = "(999+999)"
        result = self.solution.minimizeResult(expression)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
