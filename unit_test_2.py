import unittest
from factorial import factorial


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(factorial(-1), 1)


if __name__ == '__main__':
    unittest.main()
