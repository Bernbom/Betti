def swap(A,i,j):
    """
    in matrix A: swap row i and j
    """
    temp = A.getrow(i)
    A[i,:] = A.getrowview(j)
    A[j,:] = temp

def scale(A,i,n):
    """
    in matrix A: multiply row i with n
    """
    A[i,:] *= n   

def combine(A,i,j,n):
    """
    in matrix A: add row j to row i n times
    """
    A[i,:] += n*A.getrowview(j)
