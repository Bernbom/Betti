import itertools as it

def prepare(simCom):
    """
    given the maximal faces of a simplicial complex, as a string, creates a list 
    of strings reprecenting the faces in that complex 
    """
    simCom = simCom.rstrip(' ').split(' ')
    s = set([])
    for i in xrange(len(simCom)):
        simCom[i] = simCom[i].split(',')
    # make faces
    for sim in simCom:
        sim.sort()
        for l in range(1,len(sim)+1):
            s.update(it.combinations(iter(sim),l))
    s = list(s)
    s = map(list,s)
    s = map(','.join,s)
    return s
