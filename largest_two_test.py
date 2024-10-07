import unittest
import largest_two as lt 

class Test(unittest.TestCase):
  def test_two_largest(self):
    arr = [x for x in range(1000000)]
    '''testing two_largest func'''
    self.assertEqual(lt.two_largest(arr), (999999, 999998))
