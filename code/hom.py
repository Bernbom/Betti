#import numpy as np
#import scipy.sparse
import prep
import gauss
import bound as b
import im_ker

def betti(d,simCom):
    """
    betti(d,simCom) 
    calculates the H-vector for a simplicial complex which is given as 
    a string of the maximal faces. d is the dimension of the simplicial complex
    """
    n = d+2
    f =range(n)
    H = range(n)
    bound = range(n-1)
    # find the faces of the simplex and sort them into lengths
    faces = prep.prepare(simCom)
    print "Done preparing simplexes"
    i = map(lambda face : len(face.split(',')),faces)
    for k in range(n):
        f[k] = [faces[x] for x in range(len(i)) if i[x] == k]
        f[k].sort()
    # find the boundary maps and the dimentions of the image and kernel of the 
    # maps
    dims = [(0,1)] # test
    print "Ready for boundary matrices"
    for k in range(n-1):
        print 'Making boundary matrix '+str(k)
        bound = b.boundary(f[k+1],f[k])
        print "Gauss eliminating!"
        bound = gauss.elimination(bound)
        print "Calculating dimensions!"
        dims.append(im_ker.dims(bound))
    dims.append((0,0))
    # calculate the homology groups
    for k in range(n):
        H[k] = dims[k][1]-dims[k+1][0]
    return H
