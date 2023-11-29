import unittest
from tests_practice import largest, is_funny


class TrialTests(unittest.TestCase):
    def test_largest(self):
        self.assertEqual(largest([1, 4, 2, 10]), 10)
        self.assertEqual(largest(5), "You should pass a list of numbers")

    def test_is_funny(self):
        self.assertTrue(is_funny("Tim"))
        self.assertTrue(is_funny("Tammy"))
        self.assertTrue(is_funny(""))
        self.assertTrue(is_funny("Tim"))


if __name__ == "__main__":
    unittest.main()
"You should pass a list of numbers"
