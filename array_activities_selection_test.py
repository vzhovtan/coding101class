import unittest
import array_activities_selection as selection

class Test(unittest.TestCase):
  def test_findMaxActivities(self):
    '''testing findMaxActivities finction'''
    start = [1, 3, 0, 5, 8, 5] 
    fin = [2, 4, 6, 7, 9, 9] 
    self.assertListEqual(selection.findMaxActivities(start, fin), [1, 3, 5, 8])
    self.assertNotEqual(selection.findMaxActivities(start, fin), [2, 4, 6, 10])