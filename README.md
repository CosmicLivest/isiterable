<div align="center">

<h1>isiterable</h1>

**isiterable** is a Python module that provides the `isiterable` function, which acts as an object checker to know if it is iterable or not. It does not call the function and also has no undesirable performance numbers.
</div>

## Features of isiterable

- Never call `__iter__`
- Functional for generators
- It's faster than [tryiter](https://github.com/CosmicLivest/isiterable/main/README.md#try-iter) or [hasiter](https://github.com/CosmicLivest/isiterable/main/README.md#has-iter)

## Installation

```sh
pip install isiterable
```

## Usage
```py
from isiterable import isiterable


print(isiterable(57890))  # False
print(isiterable([1, "Hello!"]))  # True
```

### Using with classes

```py
from isiterable import isiterable


class NoIters:
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        # isiterable will return False, Must be a generator :/
        return self.args


class YesIters:
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        # Works!
        for arg in args:
            yield arg


x = YesIters((1, 2))
res = isiterable(x)
print(res)  # True

x = NoIters("Hello!")
res = isiterable(x)
print(res)  # False
```

### Other Examples
```py
>>> from isiterable import isiterable
>>> isiterable(b"\x00\x01...")
True
>>> isiterable(callable)
False
>>> isiterable({"key1": True})
True
>>> isiterable([])
True
```

## Alternatives to isiterable

If it doesn't match using `isiterable`, there are some solutions where you know which is better.
#### try-iter

This involves calling `__iter__`
```py
try:
    iter(object)
except TypeError:
    pass
```
#### has-iter

this will check if the object has the attribute `__iter__`
```py
if hasattr(object, "__iter__"):
    # ...
```
## Benchmark

This small benchmark uses 3 code blocks:
- [tryiter](https://github.com/CosmicLivest/isiterable/main/README.md#try-iter)
- [hasiter](https://github.com/CosmicLivest/isiterable/main/README.md#has-iter)
- `isiterable(object)`
> Where `object` is the argument to pass

Running [benchmark.py](https://github.com/CosmicLivest/isiterable/blob/branch/benchmark.md) will give results similar to this
```
Running 1,000,000 times each block of code...

Results of isiterable: 0.381
Results of hasiter   : 0.777
Results of tryiter   : 5.689
```
The best result is `isiterable` while [tryiter](https://github.com/CosmicLivest/isiterable/main/README.md#try-iter) having the worst result.
