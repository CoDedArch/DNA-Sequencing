from Genome.genome import Genome

genome = Genome("panamabananas")
pattern = "nana"

def brtforce(ptrn:str, genome: Genome):
    for sequence in genome.sequences:
        print(sequence)
