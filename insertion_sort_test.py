import unittest
import insertion_sort as insrt 

class Test(unittest.TestCase):
  def test_insertion_sort(self):
    '''testing cond function'''
    arr = [3,5,6,7,2,9]
    srted = [2, 3, 5, 6, 7, 9]
    self.assertEqual(insrt.insertion_sort(arr), srted)