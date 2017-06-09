# Drunk: Weighted Random for Python

`drunk` is a simple module that lets you make simple random operations with
customizable weights. It depends to built-in `random` module.

## Installation

Just install it via `pip`. It's compatible with 2.7 and 3.x versions of Python.

> `pip install drunk`

## Use

### `drunk.static_picker(bundle, weight_key)`

Creates a generator that chooses a random element from `bundle`
Weight for each element is calculated by the
`weight_key`. `weight_key` should
provide a positive `int` or a positive `float` value.

### `drunk.choice(bundle, weight_key)`

Choses a random element from `bundle`.
Weight for each element is calculated by the
`weight_key`. `weight_key` should
provide a positive `int` or a positive `float` value.

### `drunk.shuffle(bundle, weight_key)`

Creates a shuffled version of the `bundle`.
`weight_key` calculates the weights.
Assume `A` and `B` in `bundle`.
If `A`'s weight greater than `B`'s,
then you'll see `A` before `B` in the shuffled `bundle`,
more frequently (that means weight).

### `drunk.sample(bundle, size, weight_key)`

Gives a `size` sized sub-bundle of the bundle.
`weight_key` calculates the weights.
If `weight_key` returns a higher value for an element,
The probability of chosing that element is also higher.

---
If you don't provide a `weight_key`;

`drunk.choice` will behave like `random.choice`

`drunk.shuffle` will behave like `random.shuffle`

## Examples

**`static_picker` example**:

```python
import drunk

my_pretty_bundle = ['Alpay', 'Gandalf', 'Kenobi', 'Amca']
weight = lambda x: len(x)  # Assume that weights are related with the length

picker = static_picker(my_pretty_bundle)

choices = [next(picker) for i in range(10)]
print(choices)  # returns a list filled with 10 picks.
```

**`choice` example**:

Here's a dummy class named `ABasicClass`,
a list of some of its instances named `my_pretty_bundle`
and a `weight_key` to calculate weights.
`drunk.choice` choses an element according to
the weights which are calculated by
an inline function.


```python
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

```python
import drunk
my_pretty_list = ["Doctor Who", "Banana", "Meh", "Apple"]

print(drunk.shuffle(my_pretty_list, weight_key=lambda x: len(x)))
```

**Sampling example**: Let there be a bundle. We want random 5 elements of it. There is also a `f` function that calculates the weight of each element in bundle. Let the weight of an element is itself.

```python
import drunk
my_sexy_bundle = [1, 2, 3, 4]

print(drunk.sample(my_pretty_list, weight_key=lambda x: x))
```

Or you can get some of that bundle which means a random sized sub-bundle.

```python
import drunk
my_sexy_bundle = [1, 2, 3, 4]

print(drunk.sample(my_pretty_list, weight_key=lambda x: x))
```
