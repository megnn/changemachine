import unittest
import changemachine as tst

#Format Expect ('Change is $ 0.85', 'Here is 3 quarters, 1 dimes, 0 nickels and 0 pennies ')


class mincoins(unittest.TestCase):
    # def test_correct(self,val,string):
    #     self.assertEqual(tst.minimizecoins(val),string)

    def test_minimize_coins(self):
        self.assertEqual(tst.minimizecoins(2.22), [8, 2, 0, 2])
        #This may be broke. Chris wrote while drunk.
        with self.assertRaises(ValueError):
            tst.minimizecoins(-2.22)

    def test_format_coins(self):
        self.assertEqual(tst.format_coins(200 , [8, 2, 0, 2]), ('Change is $ 200', 'Here is 8 quarters, 2 dimes, 0 nickels and 2 pennies '))

    def test_minimize_dollars(self):
        self.assertEqual(tst.minimizedollars(24), [1, 0, 0, 4])



if __name__ == '__main__':
    unittest.main()

# test1 = mincoins()
#
# test1.test_correct(.65,('Change is $ 0.65', 'Here is 3 quarters, 1 dimes, 0 nickels and 0 pennies '))