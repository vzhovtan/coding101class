import unittest
import anagramm as an

class Test(unittest.TestCase):
  def test_anagramm(self):
    ''' testing anagramm finction'''
    self.assertTrue(an.anagramm('hello', 'olleh'))
    self.assertFalse(an.anagramm('hello', 'helle'))