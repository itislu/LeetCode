import unittest


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)]
              for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[len(text1)][len(text2)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        result = self.solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(result, expected)

    def test_example_2(self):
        text1 = "abc"
        text2 = "abc"
        expected = 3
        result = self.solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(result, expected)

    def test_example_3(self):
        text1 = "abc"
        text2 = "def"
        expected = 0
        result = self.solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(result, expected)

    def test_lecture_1(self):
        text1 = "hieroglyphology"
        text2 = "michaelangelo"
        expected = 5
        result = self.solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(result, expected)

    def test_lecture_2(self):
        text1 = "their"
        text2 = "habit"
        expected = 2
        result = self.solution.longestCommonSubsequence(text1, text2)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
