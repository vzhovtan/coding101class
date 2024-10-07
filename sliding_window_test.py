import unittest
import sliding_window as slw

class Test(unittest.TestCase):
  def test_max_sub(self):
    '''testing max sum subarray function'''
    self.assertEqual(slw.max_sub([1,2,3,4,5,6,7,8,9], 3), 24)
    self.assertNotEqual(slw.max_sub([1,2,3,4,5,6,7,8,9],3), 12)

  def test_longest_sub_same(self):
    '''testing longest substring with the same elements function'''
    self.assertEqual(slw.longest_sub_same('aaaabbcccaaaaaaadddd'), 7)
    self.assertNotEqual(slw.longest_sub_same('aaaabbcccaaaaaaadddd'), 9)
  
  def test_longest_sub_dif(self):
    '''testing longest substring with the K diff elements function'''
    self.assertEqual(slw.longest_sub_dif('abcdeefuiuiwiwwaaaa', 3), 'iwiwwaaaa')
    self.assertNotEqual((slw.longest_sub_dif('abcdeefuiuiwiwwaaaa', 3)), 'abcdeef')
