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

    #print(trans_seq)
    trans_seq_join = ''.join(trans_seq)
    print(f"Transcribed sequence = {trans_seq_join}")
    #  if 'T' in dna_seq:
    #      rna_seq = dna_seq.replace('T', 'A')
    #  if 'C' in dna_seq:
    #      rna_seq = dna_seq.replace('C', 'G')
    #  if 'G' in dna_seq:
    #      rna_seq = dna_seq.replace('G', 'C')
    # print(rna_seq)

    return 0


if __name__ == "__main__":
    sys.exit(main())
