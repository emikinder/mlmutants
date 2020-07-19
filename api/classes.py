class Ratio():
    count_mutant_dna = 0
    count_human_dna = 0
    ratio = 0

    def __init__(self, m, h, r): 
        self.count_mutant_dna = int(m)
        self.count_human_dna = int(h)
        self.ratio = r