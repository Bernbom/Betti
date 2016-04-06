import unittest
import numpy as np
import prep

class TestPrep(unittest.TestCase):

    def test_partial_0(self):
        self.assertTrue((prep.boundary(['1', '2', '3'] ,[])==np.matrix('1 1 1')).all)

    def test_partial_2(self):
        self.assertTrue((prep.boundary(['123'],['12','13','23'])==np.matrix('1;-1;1')).all)

    def test_value_error(self):
        self.assertRaises(ValueError, prep.boundary, ['12','13','23'], ['123'])

if __name__ == '__main__':
    unittest.main()
