import sys
import random


def main():
    bases = ['A', 'T', 'G', 'C']
    seq = random.choices(bases, k=100)
    dna_seq = ''.join(seq)
    print(f"DNA sequence = {dna_seq}")
    rna_seq = ""
    for i in dna_seq:
        if i == 'T':
            rna_seq += 'U'
        else:
            rna_seq += i
    print(f"RNA sequence = {rna_seq}")
    trans_seq = []
    for k in rna_seq:
        if k == "A":
            trans_seq.append("U")
        elif k == "U":
            trans_seq.append("A")
        elif k == "C":
            trans_seq.append("G")
        elif k == "G":
            trans_seq.append("C")

    # print(trans_seq)
    trans_seq_join = ''.join(trans_seq)
    print(f"Transcribed sequence = {trans_seq_join}")
    #  if 'T' in dna_seq:
    #      rna_seq = dna_seq.replace('T', 'A')
    #  if 'C' in dna_seq:
    #      rna_seq = dna_seq.replace('C', 'G')
    #  if 'G' in dna_seq:
    #      rna_seq = dna_seq.replace('G', 'C')
    # print(rna_seq)

    rna_codon = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
                 "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
                 "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
                 "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
                 "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
                 "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
                 "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
                 "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
                 "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
                 "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
                 "UAA": "STOP", "CAA": "Q", "AAA": "K", "GAA": "E",
                 "UAG": "STOP", "CAG": "Q", "AAG": "K", "GAG": "E",
                 "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
                 "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
                 "UGA": "STOP", "CGA": "R", "AGA": "R", "GGA": "G",
                 "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
                 }
    translt_protein = ''
    for i in range(0, len(trans_seq_join) - (3 + len(trans_seq_join) % 3), 3):
        if rna_codon[trans_seq_join[i:i + 3]] == "STOP":
            break
        translt_protein += rna_codon[trans_seq_join[i:i + 3]]
    print(f"Translated Protein = {translt_protein}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
