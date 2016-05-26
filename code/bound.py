import numpy as np
import scipy.sparse as sp

def boundary(a,b):
    """
    creates the boundary matrix from a to b, given as lists of strings,
    which is the coefficient of the 
    boundary functions: d_i(e_sigma) = sum((-1)**(index(i))e_sigma\i,i)
    """
    a = sl2ll(a)
    b = sl2ll(b)
    numRow = len(b)
    numCol = len(a)
    if numRow ==0:
        B = sp.dok_matrix(np.ones((1,numCol)))
    else:
        # make matrix
        B = sp.dok_matrix((numRow,numCol),dtype =np.int8)
        # insert 1's and -1's for the boundary
        for j in xrange(numCol):
            for i in xrange(len(a[j])):
                # figure out the e_sigma\i
                if i == 0:
                    tempStr = a[j][i+1:]
                elif i == len(a[j]):
                    tempStr = a[j][0:i]
                else:
                    tempStr = a[j][0:i]+a[j][i+1:]
                try:
                    # find e_sigma\j in b and calculate the sign for it
                    temp = b.index(tempStr)
                    B[temp,j]=(-1)**i
                except ValueError:
                    raise ValueError('inputs does not match: a=%s , b=%s' 
                        %(' '.join(map(str,a)), ' '.join(map(str,b))))
    return B

def sl2ll(a):
    """
    transforms a list of faces given as strings to a list of faces given as 
    lists 
    """
    return list(map(lambda s: s.split(','),a))
