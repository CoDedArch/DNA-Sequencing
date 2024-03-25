class Genome:
    def __init__(self, sequence):
        self.sequence = sequence

    @property
    def sequence(self):
        return self.sequence
    
    @sequence.setter
    def sequence(self, new_sequence):
        self.sequence = new_sequence

    def get_length(self):
        return len(self.sequence)