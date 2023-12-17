import unittest

from day5.main import part_1


class Day5Test(unittest.TestCase):
    def test_part_one(self):
        with open("test_input") as f:
            text_input = f.read()
            res = part_1(text_input)
            self.assertEqual(35, res)


if __name__ == '__main__':
    unittest.main()
