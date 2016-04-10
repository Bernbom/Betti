import numpy as np

def dims(A):
    """
    given a matrix from tri(A) returns the dimensions of its image and kernel
    """
    z = np.zeros(A.shape[1])
    imDim = [np.all(A[i,:]==z) for i in range(A.shape[0])].count(False)
    kerDim = A.shape[1]-imDim
    return imDim, kerDim
