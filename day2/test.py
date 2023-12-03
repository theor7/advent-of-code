import unittest

from day2.main import *


class Day2Test(unittest.TestCase):
    def test_part1(self):
        with open("test_input") as f:
            result = part_1(f)
            self.assertEqual(8, result)

    def test_part_1_v2(self):
        with open("test_input") as f:
            result = part_1_v2(f)
            self.assertEqual(8, result)

    def test_part_2(self):
        with open("test_input") as f:
            result = part_2(f)
            self.assertEqual(2286, result)


if __name__ == "__main__":
    unittest.main()
