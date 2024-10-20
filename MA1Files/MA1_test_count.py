# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        lst = (4, [1, [4], 4, 2, ['a', [[4], 3, 4]]])
        ''' Reasonable tests
        1. search empty lists
        2. count first, last and interior elements
        3. search for a list
        4. check that sublists on several levels are searched
        5. search non existing elements
        6. check that the list searched is not destroyed
        '''
        print('\nTests count')
        self.assertEqual(count(0, []), 0) #tests check nr 1
        self.assertEqual(count(4, lst), 5) #tests check nr 2 and 4
        self.assertEqual(count([4], lst), 2) #tests check nr 3, 4 and 6
        self.assertEqual(count(5, lst), 0) #tests check nr 5


if __name__ == "__main__":
    unittest.main()
