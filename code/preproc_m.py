import sys

def simcom_prep(m_file, target_file):
    """
    given a file containing a simplicial complex, with one maximal face per line
    split into 0-faces by tabs, returns a file containing the simplicial complex
    in one line, in a format ready for betti.py 
    """
    in_file = open(m_file)
    out_file = open(target_file,'w')

    for line in in_file:
        l = line.rstrip('\n').split('\t')
        out_file.write(','.join(l) + ' ')

    # clean up
    in_file.close()
    out_file.close()

if __name__ =="__main__":
    simcom_prep(sys.argv[1],sys.argv[2])
    print "success"
