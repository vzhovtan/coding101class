import unittest
import palindrom as pl 

class Test(unittest.TestCase):
  def test_is_plaindrom(self):
    '''testing is_plaindrom function'''
    inp_str = "madam"
    self.assertTrue(pl.is_palindrom(inp_str))