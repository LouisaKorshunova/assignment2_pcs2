#tran
from Bio.Seq import Seq
from Bio import SeqIO
lst=[]
trans=0
tranv=0
with open("/Users/makbuk/Downloads/rosalind_tran.txt", "r") as handle:
    for seq in SeqIO.parse(handle, "fasta"):
        sequ=str(seq.seq)
        lst.append(sequ)
    seq1=lst[0]
    seq2=lst[1]
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            pass
        elif seq1[i] in [['A', 'G'],['C', 'T']][seq2[i] in ['C', 'T']]:
            trans+= 1
        else:
            tranv +=1
    print (trans/tranv)
