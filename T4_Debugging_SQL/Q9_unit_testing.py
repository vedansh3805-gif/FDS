# Q9. Create a logical error and identify it using unit testing.

import unittest


def calculate_average(a, b, c):
    # Logical error: dividing by 2 instead of 3
    return (a + b + c) / 3


class TestAverage(unittest.TestCase):

    def test_average(self):
        self.assertEqual(calculate_average(10, 20, 30), 20)


if __name__ == "__main__":
    unittest.main()