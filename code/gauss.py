from scipy.sparse import dok_matrix
import row as r
import datetime

def elimination(A):
    """
    Given a sparse dok_matrix returns the gauss eliminated sparse matrix
    """
    numrows, numcols = A.shape
    row,col = 0,0
    while col < numcols and row < numrows:
        if col%100==0: # reports back far the program has come
            print str(col) + " " + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
        nonzero_relative_col = A.getcol(col)[row:,:].nonzero()[0]
        if len(nonzero_relative_col)==0:
            col += 1
            continue
        first_nonzero = nonzero_relative_col[0]+row #conversion from relative to absolute
        if first_nonzero!=row:
            r.swap(A,row,first_nonzero)
        pivot = A[row,col]
        for l in nonzero_relative_col: 
            if l!=0: # since l is realtive from offset row
                temp = A[l+row,col]
                r.scale(A,l+row,pivot)
                r.combine(A,l+row,row,-temp)
        row += 1
        col += 1
    return A
