import unittest

from day3.main import part_1


class Day3Test(unittest.TestCase):
    def test_part_1(self):
        with open("test_input") as f:
            res = part_1(f.readlines())
            self.assertEqual(4361, res)


if __name__ == "__main__":
    unittest.main()
