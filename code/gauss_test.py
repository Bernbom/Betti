import unittest
import numpy as np
import scipy.sparse as sp
import gauss

class TestGauss(unittest.TestCase):

    def test_big_matrix(self):
        A = np.matrix([[ -1, -1, -1, 0, 0, 0, 0, 0 ],
            [ 1, 0, 0, -1, -1, -1, 0, 0 ],
            [ 0, 1, 0, 1, 0, 0, -1, 0 ],
            [ 0, 0, 1, 0, 1, 0, 1, -1 ],
            [ 0, 0, 0, 0, 0, 1, 0, 1 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0 ]])
        A = sp.dok_matrix(A)
        B = np.matrix([[ 1,  0,  0, -1, -1,  0,  0,  1],
            [ 0,  1,  0,  1,  0,  0, -1,  0],
            [ 0,  0,  1,  0,  1,  0,  1, -1],
            [ 0,  0,  0,  0,  0,  1,  0,  1],
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [ 0,  0,  0,  0,  0,  0,  0,  0]])
        B = sp.dok_matrix(B)
        A_gauss = gauss.elimination(A)
        self.assertTrue((A_gauss-B).nnz==0)

    def test_one_column(self):
        A = sp.dok_matrix(np.matrix([[1],[-1],[1]]))
        B = sp.dok_matrix(np.matrix([[1],[0],[0]]))
        self.assertTrue((gauss.elimination(A)-B).nnz==0)

    def test_one_row(self):
        A = sp.dok_matrix(np.matrix([[1, 1, 1]]))
        B = sp.dok_matrix(np.matrix([[1, 1, 1]]))
        self.assertTrue((gauss.elimination(A)-B).nnz==0)


if __name__=='__main__':
    unittest.main()
