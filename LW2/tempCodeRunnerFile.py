import unittest
from insertion_sort import insertion_sort
from merge_sort import merge_sort


class SearchTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        required_output = [1, 2, 3, 4, 5]
        input = [3, 2, 1, 5, 4]
        insertion_sort(input)
        self.assertListEqual(input, required_output)

    #     input = [5, 4, 3, 2, 1]
    #     output = [1, 2, 3, 4, 5]
    #     insertion_sort(input)
    #     self.assertListEqual(input, required_output)

    def test_merge_sort(self):
        required_output = [1, 2, 3, 4, 5]
        input = [3, 2, 1, 5, 4]
        merge_sort(input,0,len(required_output)-1)
        self.assertListEqual(input, required_output)

    #     input = [5, 4, 3, 2, 1]
    #     output = [1, 2, 3, 4, 5]
    #     merge_sort(input)
    #     self.assertListEqual(input, required_output)


if __name__ == '__main__':
    unittest.main()
