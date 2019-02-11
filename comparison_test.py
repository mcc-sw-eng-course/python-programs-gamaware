import unittest
import comparison

class TestComparisons(unittest.TestCase):

    def test_comparison(self):
        self.assertEqual(comparison.compareFiles(), "The files are the same")

if __name__ == '__main__':
    unittest.main()