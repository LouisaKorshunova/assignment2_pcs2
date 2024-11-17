#splc
from Bio import SeqIO
lst=[]
with open("/Users/makbuk/Downloads/rosalind_splc.txt", "r") as handle:
    for seq in SeqIO.parse(handle, "fasta"):
        id=seq.id
        sequ=str(seq.seq.transcribe())
        lst.append(sequ)
    dna=lst[0]
    exo=lst[1:]
    for i in range(len(exo)):
        dna=dna.replace(exo[i],'')
    
    def translate(dna): 
        table={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
        protein ="" 
        if len(dna)%3 == 0: 
            for i in range(0, len(dna), 3): 
                codon = dna[i:i + 3] 
                if table[codon] != "STOP":
                    protein+= table[codon] 
        return protein 
    print(translate(dna))
     
