class Genome:
    def __init__(self, sequence):
        self.sequence = sequence

    @property
    def sequences(self):
        return self.sequence
    
    @sequences.setter
    def sequences(self, new_sequence):
        self.sequence = new_sequence

    def get_length(self):
        return len(self.sequence)