#revp
import Bio.Seq as bs
with open("/Users/makbuk/Downloads/rosalind_revp.txt", "r") as Fastaseq:
    sequence=bs.Seq("".join(Fastaseq.read().strip().split("\n")[1:]).strip())
    
for i in range(len(sequence)):
    for j in range(4,13):
        if i+j<=len(sequence) and sequence[i:i+j]==bs.reverse_complement(sequence[i:i+j]):
            print(i+1,j)
