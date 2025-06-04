import string
import unittest
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        incomplete = {c: False for c in string.ascii_lowercase}
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            if s[i] in s[i + 1 :]:
                incomplete[s[i]] = True
                continue
            incomplete[s[i]] = False
            if not any(incomplete.values()):
                result.append(cur_len)
                cur_len = 0

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "ababcbacadefegdehijhklij"
        expected = [9, 7, 8]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)

    def test_example_2(self):
        s = "eccbbbbdec"
        expected = [10]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "a"
        expected = [1]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)

    def test_all_same_characters(self):
        s = "aaaa"
        expected = [4]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)

    def test_all_different_characters(self):
        s = "abcdef"
        expected = [1, 1, 1, 1, 1, 1]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)

    def test_two_partitions(self):
        s = "ababcc"
        expected = [4, 2]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)

    def test_overlapping_characters(self):
        s = "abccba"
        expected = [6]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)

    def test_repeating_partition(self):
        s = "abcabc"
        expected = [6]
        result = self.solution.partitionLabels(s)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
