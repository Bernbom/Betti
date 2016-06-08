import numpy as np
import scipy.sparse as sp

def dims(A):
    """
    given a sparse dok_matrix from gauss.elimination(A) returns the dimensions
    of its image and kernel
    """
    row, col = A.nonzero()
    im_dim = len(set(row))
    ker_dim = A.shape[1]-im_dim
    return im_dim, ker_dim
