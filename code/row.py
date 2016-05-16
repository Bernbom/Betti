import numpy as np

def swap(A,i,j):
    """
    in matrix A: swap row i and j
    """
    temp = np.copy(A[i,:])
    A[i,:] = A[j,:]
    A[j,:] = temp

def scale(A,i,n):
    """
    in matrix A: multiply row i with n
    """
    A[i,:] = n*A[i,:]   

def combine(A,i,j,n):
    """
    in matrix A: add row j to row i n times
    """
    A[i,:] += n*A[j,:]
