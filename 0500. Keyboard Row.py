import unittest
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set(iter("qwertyuiop")), set(iter("asdfghjkl")), set(iter("zxcvbnm"))]
        result = []
        for word in words:
            word_lower = word.lower()
            for row in rows:
                if row.issuperset(word_lower):
                    result.append(word)
                    break
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        words = ["Hello", "Alaska", "Dad", "Peace"]
        expected = ["Alaska", "Dad"]
        result = self.solution.findWords(words)
        self.assertEqual(result, expected)

    def test_example_2(self):
        words = ["omk"]
        expected = []
        result = self.solution.findWords(words)
        self.assertEqual(result, expected)

    def test_example_3(self):
        words = ["adsdf", "sfd"]
        expected = ["adsdf", "sfd"]
        result = self.solution.findWords(words)
        self.assertEqual(result, expected)

    def test_single_character_words(self):
        words = ["a", "s", "z"]
        expected = ["a", "s", "z"]
        result = self.solution.findWords(words)
        self.assertEqual(result, expected)

    def test_mixed_case(self):
        words = ["QwErTy", "AsDf", "ZxCv"]
        expected = ["QwErTy", "AsDf", "ZxCv"]
        result = self.solution.findWords(words)
        self.assertEqual(result, expected)

    def test_empty_input(self):
        words = []
        expected = []
        result = self.solution.findWords(words)
        self.assertEqual(result, expected)

    def test_all_invalid_words(self):
        words = ["qaz", "wsx", "edc"]
        expected = []
        result = self.solution.findWords(words)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
