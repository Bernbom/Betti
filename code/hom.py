import numpy as np
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
    i = map(len,faces)
    for k in range(n):
        f[k] = sorted(faces[x] for x in range(len(i)) if i[x] == k)
    # find the boundary maps and the dimentions of the image and kernel of the 
    # maps
    for k in range(n-1):
        bound[k] = b.boundary(f[k+1],f[k])
        bound[k] = gauss.reduce(bound[k])
    if simCom=="":
        dims = [(0,0)]+map(im_ker.dims,bound)+[(0,0)] 
    else:
        dims = [(0,1)]+map(im_ker.dims,bound)+[(0,0)] 
    # calculate the homology groups
    for k in range(n):
        H[k] = dims[k][1]-dims[k+1][0]
    return H
