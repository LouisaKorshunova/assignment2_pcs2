#lcsm
from Bio import SeqIO
lst=[]
with open("/Users/makbuk/Downloads/rosalind_lcsm.txt", "r") as handle:
    for seq in SeqIO.parse(handle, "fasta"):
        seq=str(seq.seq)
        lst.append(seq)
    motifs=''
    sorted(lst, key=len)
    shortseq=lst[0]
    compseq=lst[1:]
    for i in range(len(shortseq)):
        for j in range(i,len(shortseq)):
            presente=False
            subs=shortseq[i:j+1]
            for sequences in compseq:
                if subs in sequences:
                    presente=True
                else:
                    presente=False
                    break
            if presente and len(subs)>len(motifs):
                 motifs=subs
    print(motifs)
 
