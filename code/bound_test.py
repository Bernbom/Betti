import unittest
import numpy as np
import bound

class TestBound(unittest.TestCase):

    def test_partial_0(self):
        self.assertTrue((bound.boundary(['1', '2', '3'] ,[])==np.matrix('1 1 1')).all)

    def test_partial_2(self):
        self.assertTrue((bound.boundary(['123'],['12','13','23'])==np.matrix('1.;-1.;1.')).all)

    def test_partial_22(self):
        self.assertTrue((bound.boundary(['123', '234'],['12','13','23','24','34'])==np.matrix('1 0;-1 0;1 1;0 -1;0 1')).all)

    def test_value_error(self):
        self.assertRaises(ValueError, bound.boundary, ['12','13','23'], ['123'])

if __name__ == '__main__':
    unittest.main()
