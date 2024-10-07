import unittest
import selection_sort as sel

class Test(unittest.TestCase):

  def test_smallest(self):
    '''testing smallest function'''
    arr = [12, 13, 2, 15, 16, 10, 14, 9, 5, 18, 17, 8, 4, 11, 19, 7, 0, 3, 1, 6]
    self.assertEqual(sel.smallest(arr), 16)

  def test_sel_sort(self):
    '''testing sel_sort func'''
    arr = [12, 13, 2, 15, 16, 10, 14, 9, 5, 18, 17, 8, 4, 11, 19, 7, 0, 3, 1, 6]
    srt_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    self.assertEqual(sel.sel_sort(arr), srt_arr)  