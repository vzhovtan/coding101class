import unittest
import binary_search as bis

class Test(unittest.TestCase):
  def test_bin_search(self):
    '''testing bin_search function'''
    arr = [1,2,3,4,5,6,7,8,9]
    self.assertEqual(bis.bin_search(arr, 3), 2)
    self.assertNotEqual(bis.bin_search(arr, 4), 2)