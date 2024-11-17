#cons
import numpy as np
from Bio import SeqIO
lst=[]
cons=[]
for sequ in SeqIO.parse("/Users/makbuk/Downloads/rosalind_cons.txt", "fasta"):
    lst.append((sequ.seq))
mtx=np.array(lst)
mtx=mtx.transpose()
A,C,G,T=[],[],[],[]
for i in mtx:
    A.append(list(i).count('A'))
    C.append(list(i).count('C'))
    G.append(list(i).count('G'))
    T.append(list(i).count('T'))
profile=[]
profile.append(A)
profile.append(C)
profile.append(G)
profile.append(T)
transposeprofile=np.array(profile).transpose()
cons = []
for m in range(0,len(profile[0])):
    p = list(transposeprofile[m])
    if p.index(max(p)) == 0:
        cons.append('A')
    elif p.index(max(p)) == 1:
        cons.append('C')
    elif p.index(max(p)) == 2:
        cons.append('G')
    elif p.index(max(p)) == 3:
        cons.append('T')
print(''.join(cons))
print('A:',*A)
print('C:',*C)
print('G:',*G)
print('T:',*T)
