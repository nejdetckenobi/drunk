"""
PyDrunk is a statistically weighted random module for Python.
"""

import random


class InsufficientDataException(BaseException):
    """Insufficient Data Exception"""
    def __init__(self):
        super(InsufficientDataException, self).__init__()


class GeneticalOptimizer(object):
    """A genetical algorithm based simple optimizer class."""
    def __init__(self, initial_population, weight_function, breeding_function):
        super(GeneticalOptimizer, self).__init__()
        if len(initial_population) < 2:
            raise InsufficientDataException("Not enough unit to breed.")

        self.weight_function = weight_function
        self.breeding_function = breeding_function
        self.initial_population = initial_population
        self.population = initial_population[:]

    def breed(self):
        """
        Creates a new member and adds it to population
        """
        mom, dad = shuffle(self.population, self.weight_function)[:2]

        child = self.breeding_function(mom, dad)
        self.population.append(child)

    def generate(self, count=None, natural_selection=None):
        """
        Generates a new generation with a member count.
        """
        if not count:
            count = random.randrange(0, len(self.population))
        for _ in range(count):
            self.breed()
        if isinstance(natural_selection, int):
            sorted_pop = sorted(self.population, key=self.weight_function)
            self.population = sorted_pop[:natural_selection]

    def fittest(self):
        """
        Returns the fittest of the population.
        """
        return max(self.population, key=self.weight_function)


def choice(bundle, weight_key=lambda x: 1):
    """
    Weighted random choice function.
    """
    cumulative_list = []
    cumulative_list.append(0)
    summation = 0
    for element in bundle:
        summation += weight_key(element)
        cumulative_list.append(summation)

    random_num = random.random() * float(summation)
    i = 0
    while cumulative_list[i] < random_num:
        i += 1
    return bundle[i-1]


def shuffle(bundle, weight_key=lambda x: 1):
    """
    Weighted random shuffle function.
    """
    badcopy = bundle[:]
    result = []
    while badcopy:
        choosen_one = choice(bundle=badcopy, weight_key=weight_key)
        result.append(choosen_one)
        badcopy.remove(choosen_one)
    return result
