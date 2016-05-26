import itertools as it

def prepare(simCom):
    """
    given the maximal faces of a simplicial complex, as a string, creates a list 
    of strings reprecenting the faces in that complex 
    """
    simCom = simCom.split(' ')
    s = set([])
    for i in xrange(len(simCom)):
        simCom[i] = simCom[i].split(',')
    # make simplexes
    for sim in simCom:
        for l in range(1,len(sim)+1):
            s.update(it.combinations(iter(sim),l))
    s = list(s)
    s = map(list,s)
    s = map(','.join,s)
    return s
