import unittest
import two_pointers as tpw

class Test(unittest.TestCase):
  def test_pair_sum(self):
    '''testing pari sum finction'''
    arr = [1,2,3,4,5,6,7,8,9]
    self.assertEqual(tpw.pair_sum(arr, 6), [(1, 5), (2, 4)])
    self.assertNotEqual(tpw.pair_sum(arr, 6), [(1, 6), (3, 4)])

  def test_triplet_zero(self):
    '''testing triplet_zero function'''
    a1 = [-1, -2, -3, -4, -5, -6, -7, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a2 = [(-1, -2, 3), (-1, -3, 4), (-1, -4, 5), (-1, -5, 6), (-1, -6, 7), (-1, -7, 8), \
      (-2, -3, 5), (-2, -4, 6), (-2, -5, 7), (-2, -6, 8), (-2, -7, 9), (-3, -4, 7), \
        (-3, -5, 8), (-3, -6, 9), (-3, 1, 2), (-4, -5, 9), (-4, 1, 3), (-5, 1, 4), \
          (-5, 2, 3), (-6, 1, 5), (-6, 2, 4), (-7, 1, 6), (-7, 2, 5), (-7, 3, 4)]
    self.assertEqual(tpw.triplet_zero(a1), a2)