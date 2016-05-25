import numpy as np
import scipy.sparse as sp

def dims(A):
    """
    given a sparse dok_matrix from gauss.elimination(A) returns the dimensions
    of its image and kernel
    """
    row, col = A.nonzero()
    imDim = len(set(row))
#    z = np.zeros(A.shape[1])
#    imDim = [np.all(A[i,:]==z) for i in range(A.shape[0])].count(False)
    kerDim = A.shape[1]-imDim
    return imDim, kerDim
