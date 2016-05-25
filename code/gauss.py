#import numpy as np
from scipy.sparse import dok_matrix
import row

def elimination(A):
    """
    Given a sparse dok_matrix returns the gauss eliminated sparse matrix
    """
    numRows, numCols = A.shape
    i,j = 0,0
    while j < numCols and i < numRows:
        if A[i,j]==0:
            k = i
            while k<numRows:
                if A[k,j]==0:
                    k+=1
                else:
                    row.swap(A,i,k)
                    break
            if k == numRows:
                j += 1
                continue
        p = float(A[i,j]) #make p a float such that 1/p does not truncate to 0
        row.scale(A,i,1/p)
        for l in range(numRows):
            if l != i:
                n = A[l,j]
                row.combine(A,l,i,-n)
        i += 1
        j += 1
    return A
