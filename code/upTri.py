import numpy as np
import rowOp

def tri(A):
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
                    rowOp.rowSwap(A,i,k)
                    break
            if k == numRows:
                j += 1
                continue
        p = float(A[i,j])
        rowOp.rowScale(A,i,1/p)
        for l in range(numRows):
            if l != i:
                n = A[l,j]
                rowOp.rowCombine(A,l,i,-n)
        i += 1
        j += 1
    return A
