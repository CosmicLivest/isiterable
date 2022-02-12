"""
Simple benchmark to check if an object is verifiable, using these blocks::

    Using try-except syntax
    >>> try:
    >>>     iter(argument)
    >>> except:
    >>>     pass

    Using builtins.hastattr
    >>> hasattr(argument, "__iter__")

    Using isiterable.isiterable
    >>> isiterable(argument)
"""

import timeit


argument = 57890

isiterable_code = f"isiterable({argument!r})"
hasiter_code = f"hasattr({argument!r}, '__iter__')"
tryiter_code = f"try: iter({argument!r})\nexcept: pass"


print("Running 1,000,000 times each block of code...\n")
res_isiterable = timeit.timeit(
    isiterable_code, "from isiterable import isiterable"
)
res_hasiter = timeit.timeit(hasiter_code)
res_tryiter = timeit.timeit(tryiter_code)

print(f"Results of isiterable: {res_isiterable:.3f}")
print(f"Results of hasiter   : {res_hasiter:.3f}")
print(f"Results of tryiter   : {res_tryiter:.3f}")
