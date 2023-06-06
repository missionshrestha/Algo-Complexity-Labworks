import unittest
from linear_search import linear_search
from binary_search import binary_search


class SearchTestCase(unittest.TestCase):
    def test_linear_search(self):
        values = [5, 3, 6, 1, 4, 9, 0]
        # res = linear_search(values, 6)
        # self.assertEqual(res, 2)
        res = linear_search(values, 3)
        self.assertEqual(res, 1)

    def test_binary_search(self):
        values = [0, 1, 2, 3, 4, 5]
        # res = binary_search(values, 6)
        # self.assertEqual(res, 2)
        res = binary_search(values, 3, 0, len(values))
        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()
