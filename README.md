Drunk: Weighted Random for Python
=================================
`drunk` is a simple module that lets you make simple random operations with
customizable weights. It is dependent to built-in `random` module.

## Classes
###### `GeneticalOptimizer(initial_population, weight_key, breeding_function)`
A basic implemention for genetical algorithms.

`initial_population` is the startup population which should
be larger than 2 units. Otherwise, that'll cause an error
named `InsufficientDataError`.

`weight_key` is a function that calculates a fit score
for every single chromosome in the population. Must be able
to take a chromosome and must return a scalar value.

`breeding_function` is also a function which should be able
to take 2 chromosome, crossover them and return the new
chromosome.


## Functions
###### `drunk.choice(bundle, weight_key)`
Choses a random element from `bundle`.
Weight for each element is calculated by the
`weight_key`. `weight_key` should
provide a positive `int` or a positive `float` value.
###### `drunk.shuffle(bundle, weight_key)`
Creates a shuffled version of the `bundle`.
`weight_key` calculates the weights.
Assume `A` and `B` in `bundle`.
If `A`'s weight greater than `B`'s,
then you'll see `A` before `B` in the shuffled `bundle`,
more frequently (that means weight).
###### `drunk.sample(bundle, size, weight_key)`
Gives a `size` sized sub-bundle of the bundle.
`weight_key` calculates the weights.
If `weight_key` returns a higher value for an element,
The probability of chosing that element is also higher.

---
If you don't provide a `weight_key`;

`drunk.choice` will behave like `random.choice`

`drunk.shuffle` will behave like `random.shuffle`

## Examples
**Choice example**:
Here's a dummy class named `ABasicClass`,
a list of some of its instances named `my_pretty_bundle`
and a `weight_key` to calculate weights.
`drunk.choice` choses an element according to
the weights which are calculated by
an inline function.


```Python3
import drunk

class ABasicClass(object):
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
	def __repr__(self):
		return str(self.name)

my_pretty_bundle = []
my_pretty_bundle.append(ABasicClass("Amca", 40))
my_pretty_bundle.append(ABasicClass("Alpay", 30))
my_pretty_bundle.append(ABasicClass("Gandalf", 20))
my_pretty_bundle.append(ABasicClass("Kenobi", 10))

choosen_one = drunk.choice(my_pretty_bundle, lambda x: x.weight)
print("You picked ", choosen_one, "!!1!one!")
```

**Shuffle example**:
Here's an list named `my_pretty_list`.
The weight of an element is its length.

```Python3
import drunk
my_pretty_list = ["Doctor Who", "Banana", "Meh", "Apple"]

print(drunk.shuffle(my_pretty_list, weight_key=lambda x: len(x)))
```

**Sampling example**: Let there be a bundle. We want random 5 elements of it. There is also a `f` function that calculates the weight of each element in bundle. Let the weight of an element is itself.

```Python3
import drunk
my_sexy_bundle = [1,  2, 3, 4]

print(drunk.sample(my_pretty_list, weight_key=lambda x: x))
```

Or you can get some of that bundle which means a random sized sub-bundle.

```Python3
import drunk
my_sexy_bundle = [1, 2, 3, 4]

print(drunk.sample(my_pretty_list, weight_key=lambda x: x))
```


**Genetical Optimizer example**: Let there be a function _f_
(which is actually a `weight_key`).
We wish to maximize that function in __[a,b]__.

Assume that `f(x) = -(x ** 2)` and `[a,b] = [1 , 5]`.
(We know the f's analytical optimum point in that borders.)
We take the breeding function as `g(a, b) = (a + b) / 2`

```python
from drunk import GeneticalOptimizer
g = GeneticalOptimizer([1,5],
					   lambda x: - (x ** 2),
					   lambda a,b: (a+b)/2)
# You can add more points if you wish. Like [1,2,3,5] but not larger than 5 and
# not smaller than 1, because of our borders.

g.generate(count=100, # 100 generation, not 100 breed! This means a lot.
		   natural_selection=100) # Population capacity supports 100 fit breeds.

result = g.fittest()
print(result) # prints the solution.
```
Note that genetical algorithms are applicable just for detecting
if there is a solution. You can use it for iterable solutions more efficiently.
But you should define the `weight_key` and the `breeding_function` properly.
The system's success rate and performance depends on the `weight_key`'s
definition.
