import string
import unittest
from functools import cache


class Solution:
    def minimumDistance(self, word: str) -> int:
        @cache
        def dp(i: int, f1: str, f2: str) -> int:
            if i == len(word):
                return 0
            return min(
                Solution.distance(f1, word[i]) + dp(i + 1, word[i], f2),
                Solution.distance(f2, word[i]) + dp(i + 1, f1, word[i]),
            )

        return dp(0, "", "")

    keyboard = {c: (i // 6, i % 6) for i, c in enumerate(string.ascii_uppercase)}

    @cache
    @staticmethod
    def distance(src: str, dst: str) -> int:
        if src == "":
            return 0
        (x1, y1), (x2, y2) = Solution.keyboard[src], Solution.keyboard[dst]
        return abs(x1 - x2) + abs(y1 - y2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        word = "CAKE"
        expected = 3
        result = self.solution.minimumDistance(word)
        self.assertEqual(result, expected)

    def test_example_2(self):
        word = "HAPPY"
        expected = 6
        result = self.solution.minimumDistance(word)
        self.assertEqual(result, expected)

    def test_two_letters(self):
        word = "AB"
        expected = 0
        result = self.solution.minimumDistance(word)
        self.assertEqual(result, expected)

    def test_same_letters(self):
        word = "AAA"
        expected = 0
        result = self.solution.minimumDistance(word)
        self.assertEqual(result, expected)

    def test_adjacent_letters(self):
        word = "ABC"
        expected = 1
        result = self.solution.minimumDistance(word)
        self.assertEqual(result, expected)

    def test_timeout(self):
        word = "ALKDFJEWLKFBSCXVMBWEKJQOIDFKLXNCVMJKBQERASKLDFKJABSDKJBWKJBKJHKJHXCKVBKMWBEMRBKBFKSNVASDFLKHWEKLRHKSDJFKANDSFKLJASKDFJJSDJFHKJHEWRHQIUERHWBDFKXBCVBXCNKBVKWBKEBFKQYYXCVBNMAASDFHKJLGQWERIOUPTZ"
        expected = 364
        result = self.solution.minimumDistance(word)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
