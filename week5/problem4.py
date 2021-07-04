import random
import sys

"""
Notes:
- Well done!
- The only thing I would strongly suggest is to give some consideration into how you name variables. 
Variable names matter a lot. You don't want them to be too long but you also want them to be 
immediately obvious what they refer to. Avoid ad hoc abbreviations; better have a set of full words 
e.g. 'dna_sequence' than 'dna_seq' which has its own meaning, or better simply 'dna'. Naming is 
an art but perhaps the best way to spend time cleaning up your code. The legibility of Python 
allows you to keep things nice and clean. 
- The main benefit of using git is that commits save snapshot of the repository. Use this to your 
advantage. Always commit the complete state e.g. once it is just barely working do a commit then 
for each improvement do another commit. This will allow you to always have things clean. Once you 
have it working correctly you can then pay attention to variable names for the final commits. 
If you were not working with git then you would have to keep track of all the states of the 
module by commenting things out. No need for this with git. 
"""


def main():
    bases = ['A', 'T', 'G', 'C']
    seq = random.choices(bases, k=100)
    dna_seq = ''.join(seq)
    print(f"DNA sequence = {dna_seq}")
    rna_seq = ""
    # todo: is there a string method that can replace the following 5 lines?
    for i in dna_seq:
        if i == 'T':
            rna_seq += 'U'
        else:
            rna_seq += i
    print(f"RNA sequence = {rna_seq}")
    # todo: which string method can perform transcription for you?
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
    # fixme: the following lines should be in old commits and should not be here
    #  if 'T' in dna_seq:
    #      rna_seq = dna_seq.replace('T', 'A')
    #  if 'C' in dna_seq:
    #      rna_seq = dna_seq.replace('C', 'G')
    #  if 'G' in dna_seq:
    #      rna_seq = dna_seq.replace('G', 'C')
    # print(rna_seq)
    # fixme: instead of 'rna_codon' consider 'genetic_code'
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
    # fixme: it is better to have long variable names than ad hoc abbreviations; for example instead of 'translt_protein' better is
    #  'translated_protein' or simply 'protein'
    translt_protein = ''
    for i in range(0, len(trans_seq_join) - (3 + len(trans_seq_join) % 3), 3):
        if rna_codon[trans_seq_join[i:i + 3]] == "STOP":
            break
        translt_protein += rna_codon[trans_seq_join[i:i + 3]]
    print(f"Translated Protein = {translt_protein}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
