import unittest
import numpy as np
import scipy.sparse as sp
import gauss

class TestGauss(unittest.TestCase):

    def test_one_column(self):
        A = sp.lil_matrix(np.matrix([[1],[-1],[1]]))
        B = sp.lil_matrix(np.matrix([[1],[0],[0]]))
        self.assertTrue((gauss.elimination(A)-B).nnz==0)

    def test_one_row(self):
        A = sp.lil_matrix(np.matrix([[1, 1, 1]]))
        B = sp.lil_matrix(np.matrix([[1, 1, 1]]))
        self.assertTrue((gauss.elimination(A)-B).nnz==0)
        
    def test_full_matrix(self):
        A = np.matrix([
            [2, 3, 4],
            [5, 6, 7],
            [8, 9, 10]])
        A = sp.lil_matrix(A)
        B = np.matrix([
            [2, 3, 4],
            [0, -3, -6],
            [0, 0, 0]])
        B = sp.lil_matrix(B)
        self.assertTrue((gauss.elimination(A)-B).nnz==0)

if __name__=='__main__':
    unittest.main()
