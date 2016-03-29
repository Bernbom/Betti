import numpy as np
import upTri

A = np.matrix('-1 -1 -1 0 0 0 0 0; 1 0 0 -1 -1 -1 0 0; 0 1 0 1 0 0 -1 0; 0 0 1 0 1 0 1 -1; 0 0 0 0 0 1 0 1; 0 0 0 0 0 0 0 0')
upTri.tri(A)
