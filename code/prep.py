import numpy as np
import itertools as it

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
