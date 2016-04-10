import unittest
import numpy as np
import upTri

class TriTest(unittest.TestCase):

    def test_big_matrix(self):
        A = np.matrix([[ -1, -1, -1, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        B = np.matrix([[ 1,  0,  0, -1, -1,  0,  0,  1],
            [ 0,  1,  0,  1,  0,  0, -1,  0],
            [ 0,  0,  1,  0,  1,  0,  1, -1],
            [ 0,  0,  0,  0,  0,  1,  0,  1],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0]])
        self.assertTrue((upTri.tri(A)==B).all)

    def test_one_column(self):
        A = np.matrix([[1],[-1],[1]])
        B = np.matrix([[1],[0],[0]])
        self.assertTrue((upTri.tri(A)==B).all)

    def test_one_row(self):
        A = np.matrix([[1, 1, 1]])
        B = np.matrix([[1, 1, 1]])
        self.assertTrue((upTri.tri(A)==B).all)


if __name__=='__main__':
    unittest.main()
