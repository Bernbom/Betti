import sys

def simcom_prep(off_file, target_file):
    """
    given an off file containing a simplicial complex returns a file containing 
    the simplicial complex in one line in a format ready for betti.py 
    """
    in_file = open(off_file)
    out_file = open(target_file,'w')

    offline = in_file.readline()
    [vertices, faces, edges] = in_file.readline().rstrip('\n').split()
    trash = in_file.readline() # possibly empty line
    if trash == "\n":
        for vertice in xrange(int(vertices)):
            in_file.next()
            out_file.write(str(vertice) + ' ')
        for face in xrange(int(faces)):
            line = in_file.next()
            line = line.rstrip('\n').split()
            out_file.write(','.join(line[1:]) + ' ')
    else:
        for vertice in xrange(int(vertices)-1):
            in_file.next()
            out_file.write(str(vertice) + ' ')
        out_file.write(str(vertice+1) + ' ')
        for face in xrange(int(faces)):
            line = in_file.next()
            line = line.rstrip('\n').split()
            out_file.write(','.join(line[1:]) + ' ')
    # clean up
    in_file.close()
    out_file.close()

if __name__ =="__main__":
    simcom_prep(sys.argv[1],sys.argv[2])
    print "success"
