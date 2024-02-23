import unittest

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(2.5, 3.5), 6)

def add_numbers(num1, num2):
    return num1 + num2

if __name__ == '__main__':
    unittest.main()
