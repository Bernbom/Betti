import unittest
import numpy as np
import bound

class TestBound(unittest.TestCase):

    def test_partial_0(self):
        self.assertTrue((bound.boundary(['1', '2', '3'] ,[])==np.matrix('1 1 1')).all)

    def test_partial_2(self):
        self.assertTrue((bound.boundary(['1,2,3'],['1,2','1,3','2,3'])==np.matrix('1.;-1.;1.')).all)

    def test_partial_22(self):
        self.assertTrue((bound.boundary(['1,2,3', '2,3,4'],['1,2','1,3','2,3','2,4','3,4'])==np.matrix('1 0;-1 0;1 1;0 -1;0 1')).all)

    def test_value_error(self):
        self.assertRaises(ValueError, bound.boundary, ['1,2','1,3','2,3'], ['123'])

if __name__ == '__main__':
    unittest.main()
