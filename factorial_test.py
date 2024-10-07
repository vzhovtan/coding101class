import unittest
import factorial

class Test(unittest.TestCase):
  def test_fact(self):
    '''testing fact function'''
    self.assertEqual(factorial.fact(5), 120)