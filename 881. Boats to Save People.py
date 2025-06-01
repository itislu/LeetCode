import unittest
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        low = 0
        high = len(people) - 1
        while low <= high:
            boats += 1
            if people[high] + people[low] <= limit and high != low:
                low += 1
            high -= 1
        return boats


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        people = [1, 2]
        limit = 3
        expected = 1
        result = self.solution.numRescueBoats(people, limit)
        self.assertEqual(result, expected)

    def test_example_2(self):
        people = [3, 2, 2, 1]
        limit = 3
        expected = 3
        result = self.solution.numRescueBoats(people, limit)
        self.assertEqual(result, expected)

    def test_example_3(self):
        people = [3, 5, 3, 4]
        limit = 5
        expected = 4
        result = self.solution.numRescueBoats(people, limit)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
