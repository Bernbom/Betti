import itertools as it

def prepare(simCom):
    """
    given the maximal faces of a simplicial complex, as a string, creates a list 
    of strings reprecenting the faces in that complex 
    """
    simCom = simCom.split(' ')
    simCom = list(map(lambda s: s.split(','),simCom))
    s = simCom
    for sim in simCom:
        for l in range(1,len(sim)):
            s = s + list(it.combinations(iter(sim),l))
    s = map(list,s)
    s = map(','.join,s)
    s = list(set(s))
    return s
