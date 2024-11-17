#mrna
def rna_combinations(protein):
    codon_table = {
        'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4, 'H': 2,
        'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2, 'V': 4,
        'A': 4, 'D': 2, 'E': 2, 'G': 4, 'Stop': 3
    }

    with open('/Users/makbuk/Downloads/rosalind_mrna.txt', 'r') as file:
        lines = file.readlines()
    protein = lines[0].strip()

    total_combinations = 1
    for aa in protein:
        total_combinations *= codon_table[aa]
        total_combinations %= 1_000_000
    total_combinations *= codon_table['Stop']
    total_combinations %= 1_000_000

    return total_combinations


result = rna_combinations(protein)
print(result)

