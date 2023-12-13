import unittest

from day4.main import part_1, part_2


class TestDay4(unittest.TestCase):
    def test_part_1(self):
        with open("test_input") as f:
            line_array = f.readlines()
        result = part_1(line_array)

        self.assertEqual(13, result)

    def test_part_2(self):
        with open("test_input") as f:
            line_array = f.readlines()
        result = part_2(line_array)

        self.assertEqual(30, result)


if __name__ == "__main__":
    unittest.main()
