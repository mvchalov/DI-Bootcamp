import random


class Gene:
    def __init__(self, value=False):
        self.gene = value

    def mutate_gen(self):
        self.gene = not self.gene


class Chromosome:
    def __init__(self, value=None):
        if value is None:
            self.chromosome = []
            for i in range(10):
                initial_gene = True if random.randint(0, 1) == 1 else False
                self.chromosome.append(Gene(initial_gene))
        else:
            self.chromosome = value

    def mutate(self):
        for i in range(random.randint(0,len(self.chromosome) - 1), random.randint(0,len(self.chromosome) - 1)):
            if random.randint(0, 1) == 1:
                self.chromosome[i].mutate_gen()


class DNA(Chromosome):
    def __init__(self, value=None):
        if value is None:
            self.chromosomes = []
            for i in range(10):
                super().__init__()
                self.chromosomes.append(self.chromosome)
        else:
            self.chromosomes = value

    def mutate(self):
        for i in range(len(self.chromosomes)):
            if random.randint(0, 1) == 1:
                self.chromosome = self.chromosomes[i]
                super().mutate()
                self.chromosomes[i] = self.chromosome


class Organism:
    def __init__(self, dna=None, environment=.2):
        if dna is None:
            self.dna = DNA()
        else:
            self.dna = dna
        self.environment = environment

    def probably_mutate(self):
        if random.random() <= self.environment:
            self.dna.mutate()


guinea_pig = Organism()
turns = 0
while turns < 10000001:
    dna_formula = 0
    counter = 0
    for chromosome in guinea_pig.dna.chromosomes:
        for gene in chromosome:
            counter += 1
            if gene.gene:
                dna_formula += 1
    if dna_formula == counter:
        break
    else:
        guinea_pig.probably_mutate()
        turns += 1
    print(turns, dna_formula, counter)

if dna_formula == counter:
    print(f"It took {turns} iterations to reach a DNA which is only made of 1s.")
else:
    print(f"The Probability theory works well! We tried {turns} times and never reached the DNA which is only made of 1s.")

