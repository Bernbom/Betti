import numpy as np
import row

def reduce(A):
    """
    Given a matrix returns an upper triangle-matrix with 1's or 0's
    in the diagonal
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
        p = float(A[i,j])
        row.scale(A,i,1/p)
        for l in range(numRows):
            if l != i:
                n = A[l,j]
                row.combine(A,l,i,-n)
        i += 1
        j += 1
    return A
