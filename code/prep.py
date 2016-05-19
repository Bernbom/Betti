import itertools as it

def prepare(simCom):
    """
    given the maximal faces of a simplicial complex, as a string, creates a list 
    of strings reprecenting the faces in that complex 
    """
    simCom = simCom.split(' ')
    for i in xrange(len(simCom)):
        simCom[i] = simCom[i].split(',')
    s = simCom
    print "ready for combinations!"
    for sim in simCom:
        for l in range(1,len(sim)):
            s = s + list(it.combinations(iter(sim),l))
    s = map(list,s)
    print "ready to join"
    s = map(','.join,s)
    s = list(set(s))
    return s
