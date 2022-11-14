import unittest
from factorial import factorial


class TestCase(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(factorial(0), 1)

    def testCase2(self):
        self.assertEqual(factorial(1), 1)

    def testCase3(self):
        self.assertEqual(factorial(5), 120)


if __name__ == '__main__':
    unittest.main()
