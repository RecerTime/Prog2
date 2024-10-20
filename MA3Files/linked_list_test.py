# https://docs.python.org/3/library/unittest.html
"""
Unittests for the linked lists methods 

"""

import unittest

from linked_list import *


class Test(unittest.TestCase):

    def test_length(self): #
        lst = LinkedList()
        self.assertEqual(lst.length(), 0)
        lst.insert(3)
        self.assertEqual(lst.length(), 1)
        lst.insert(2)
        self.assertEqual(lst.length(), 2)
    
    def test_mean(self): #
        lst = LinkedList()
        lst.insert(3)
        self.assertEqual(lst.mean(), 3)
        lst.insert(2)
        self.assertEqual(lst.mean(), 2.5)

    def test_remove_last(self): #
        lst = LinkedList()
        for x in [3, 1, 2, 6]:
            lst.insert(x)

        self.assertEqual(lst.remove_last(), 6)
        self.assertEqual(lst.remove_last(), 3)
        self.assertEqual(lst.remove_last(), 2)
        self.assertEqual(lst.remove_last(), 1)
        self.assertEqual(lst.length(), 0)

    def test_remove(self): #
        lst = LinkedList()
        for x in [3, 1, 2, 6, 1]:
            lst.insert(x)

        self.assertEqual(lst.remove(0), False)
        self.assertEqual(lst.remove(1), True)
        self.assertEqual(lst.remove(1), True)
        self.assertEqual(lst.remove(3), True)
        self.assertEqual(lst.remove(3), False)
        self.assertEqual(lst.remove(2), True)
        self.assertEqual(lst.remove(2), False)

    def test_to_list(self): #
        lst = LinkedList()
        self.assertEqual(lst.to_list(), [])
        lst.insert(1)
        self.assertEqual(lst.to_list(), [1])
        for x in [1, 2, 6]:
            lst.insert(x)
        self.assertEqual(lst.to_list(), [1, 1, 2, 6])

    def test_remove_all(self): #
        lst = LinkedList()
        for x in [1, 1, 2, 6, 6, 8, 9, 9]:
            lst.insert(x)
        lst.remove_all(5)
        self.assertEqual(lst.to_list(), [1, 1, 2, 6, 6, 8, 9, 9])
        lst.remove_all(9)
        self.assertEqual(lst.to_list(), [1, 1, 2, 6, 6, 8])
        lst.remove_all(1)
        self.assertEqual(lst.to_list(), [2, 6, 6, 8])
        lst.remove_all(2)
        self.assertEqual(lst.to_list(), [6, 6, 8])
        lst.remove_all(8)
        self.assertEqual(lst.to_list(), [6, 6])
        lst.remove_all(6)
        self.assertEqual(lst.to_list(), [])


    def test___str__(self): #
        lst = LinkedList()
        self.assertEqual(str(lst), '()')
        lst.insert(1)
        self.assertEqual(str(lst), '(1)')
        lst.insert(2)
        self.assertEqual(str(lst), '(1, 2)')

    def test_copy(self):
        lst = LinkedList()
        cpy = lst.copy()
        self.assertEqual(cpy.first, None) #Copy of empty list is not working
        self.assertNotEqual(lst, cpy) #Not a new LinkedList object
        for x in [1, 1, 3, 7, 9, 2, 8]:
            lst.insert(x)
        cpy = lst.copy()
        self.assertNotEqual(lst, cpy) #Not a new LinkedList object
        orig_node = lst.first
        copy_node = cpy.first
        while orig_node and copy_node:
            self.assertNotEqual(orig_node, copy_node) #Shared nodes
            self.assertEqual(orig_node.data, copy_node.data) #Not the same data
            orig_node = orig_node.succ
            copy_node = copy_node.succ
        self.assertEqual(orig_node, copy_node) #Original and copy of different length


if __name__ == "__main__":
    unittest.main()
