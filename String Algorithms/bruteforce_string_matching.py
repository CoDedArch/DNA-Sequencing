from genome import Genome
genome = Genome("panamabananas")
pattern = "nana"

def brtforce(ptrn:str, genome: Genome):
    sequences = genome.sequences
    for pos, sequence in enumerate(sequences):
        print(sequence)
        if sequence == ptrn[0]:
            subseq = sequences[pos: len(ptrn)+2]
            print('subsque is ', subseq)
            if subseq == ptrn:
                print(f"Pattern found at position {pos}")
            else:
                print(f"Pattern not found at position {pos}") 

brtforce(pattern, genome)

