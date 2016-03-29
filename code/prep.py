import numpy as np
import itertools as it

def boundary(a,b):
    """
    boundary(a,b)
    creates the boundary matrix from a to b, given as lists of strings,
    which is the coefficient of the 
    boundary functions: d_i(e_sigma) = sum((-1)**(index(i))e_sigma\i,i)
    """
    numRow = len(b)
    numCol = len(a)
    if numRow ==0:
        B = np.ones((1,numCol))
    else:
        # make matrix
        B = np.zeros((numRow,numCol))
        # insert 1's and -1's for the boundary
        for j in range(numCol):
            for i in range(len(a[j])):
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
                    print "inputs does not match"
    return B

def prepare(simCom):
    """
    prepare(str) --> list(str)
    given the maximal faces of a simplicial complex creates a list of faces in 
    that complex 
    """
    simCom = simCom.split(' ')
    s = simCom
    for sim in simCom:
        for l in range(1,len(sim)):
            s = s + list(it.combinations(iter(sim),l))
    s = map(list,s)
    s = map(''.join,s)
    s = list(set(s))
    #s.sort(key=len, reverse=True)
    return s
