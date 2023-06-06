import unittest
from greedy import greedy
from brute_force import knapSackFractional, knapSack01


class KnapSackTestCase(unittest.TestCase):
    def test_greedy(self):

        box = [
            {"profit": 60, "weight": 10},
            {"profit": 100, "weight": 20},
            {"profit": 120, "weight": 30},
        ]
        size = 50
        profit = greedy(box, size)
        print(profit)

        self.assertEqual(profit, 240)

    def test_brute(self):

        box = [
            {"profit": 60, "weight": 10},
            {"profit": 100, "weight": 20},
            {"profit": 120, "weight": 30},
        ]
        size = 50
        fractionalProfit = knapSackFractional(len(box), box, size, 0)
        print(fractionalProfit)
        self.assertEqual(fractionalProfit, 240)
        zeroneProfit = knapSack01(len(box), box, size, 0)
        print(zeroneProfit)
        self.assertEqual(zeroneProfit, 220)


if __name__ == "__main__":
    unittest.main()
