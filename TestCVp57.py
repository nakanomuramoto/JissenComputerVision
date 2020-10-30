#coding: utf-8

import numpy as np

# fp = [[-10,1], [2, -3], [9,15], [-3, 20]]
fp = [[-10, 2, 9, -3], [1, -3, 15, 20], [1, 1, 1, 1]]

m = np.mean(fp[:2], axis=1)
maxstd = np.max(np.std(fp[:2], axis=1))  + 1e-9

C1 = np.diag([1/maxstd, 1/maxstd, 1])
C1[0][2] = -m[0] / maxstd
C1[1][2] = -m[1] / maxstd

print( "fp:")   
print( fp) 
print( "\nm (mean) :" )
print( m )
print( "\nmaxstd (max standard):" )
print( maxstd )
print( "\nC1 (diag[1/maxstd)]):" ) 
print( C1 )

# fp = np.insert(fp, 2, 1, axis=0)
# print( "\nfp:")   
# print( fp) 

fp = np.dot(C1, fp)
print( "\nnormiezd fp:" )
print( fp )
