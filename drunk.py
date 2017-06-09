"""
PyDrunk is a statistically weighted random module for Python.
"""

import random


class InsufficientDataException(BaseException):
    """Insufficient Data Exception"""
    def __init__(self):
        super(InsufficientDataException, self).__init__()


def static_picker(bundle, weight_key=lambda x: 1):
    """
    Weighted random choice generator for static bundles.
    Does the same thing with but faster than 'choice' method.
    Because weights are calculated only once.
    In return, you cannot mutate the bundle.
    It is simply a die. Returns a generator.

    weight_key: A function that calculates the weight of each element in bundle

    >>> b = [1, 2, 3]
    >>> weight = lambda x: x ** 2  # Assume that weights are square values.
    >>> g = static_picker(b)
    >>> [next(g) for i in range(10)]
    [1, 3, 1, 2, 3, 3, 1, 2, 3, 2]
    """
    bundle = bundle[:]
    if not len(bundle):
        raise InsufficientDataException('There is nothing in bundle to pick.')
    cumulative_list = [0]
    summation = 0
    for element in bundle:
        summation += weight_key(element)
        cumulative_list.append(summation)
    while True:
        i = 0
        random_num = random.random() * float(summation)
        while cumulative_list[i] < random_num:
            i += 1
        yield cumulative_list[i]


def choice(bundle, weight_key=lambda x: 1):
    """
    Weighted random choice function.
    weight_key: A function that calculates the weight of each element in bundle
    with_index: This is just for optimization. Using is not recommended.
    """
    if not len(bundle):
        raise InsufficientDataException('There is nothing in bundle to pick.')
    cumulative_list = [0]
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
    weight_key: A function that calculates the weight of each element in bundle
    """
    badcopy = bundle[:]
    result = []
    while badcopy:
        choosen_one = choice(bundle=badcopy, weight_key=weight_key,
                             with_index=True)
        result.append(choosen_one['value'])
        badcopy.pop(choosen_one['index'])
    return result


def sample(bundle, size=None, weight_key=lambda x: 1):
    """
    Weighted random sample function.
    bundle: The iterative object that you want a sample from.
    size: Size of the sample. If not given, it'll be a random value
    weight_key: A function that calculates the weight of each element in bundle
    """
    if not size:
        size = random.randrange(len(bundle))
    badcopy = bundle[:]
    result = []
    for i in range(size):
        choosen_one = choice(bundle=badcopy, weight_key=weight_key,
                             with_index=True)
        result.append(choosen_one['value'])
        badcopy.pop(choosen_one['index'])
    return result
