import sys
import hom

if __name__ =="__main__":
    simcom_file = open(sys.argv[2])
    simcom = simcom_file.readline()
    print str(hom.betti(int(sys.argv[1]),simcom))
