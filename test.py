from isiterable import isiterable


default_args = ["Hello!", object(), object(), []]


class ListArgs:
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        # works!
        for arg in self.args:
            yield arg


class NoYieldListArgs:
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        # Doesn't work :/
        # isiterable should not call the object to check it.
        return self.args


class InvalidIterator:
    def __init__(self):
        pass

    def __iter__(self):
        return


# TypeError: 'type' object is not iterable
class WithoutInitializationIterator:
    pass


line = 0
# ============= ListArgs =============
print(f"{line:04d} | Running ListArgs tests...")
for n in range(2000):
    line += 1
    x = ListArgs(*default_args)
    try:
        assert isiterable(x)
    except AssertionError:
        print(f"{line:04d} | Test ListArgs ({n}) failed")
        raise SystemExit
    print(f"{line:04d} | Test ListArgs ({n}) passed")


# ============= NoYieldListArgs =============
line += 1
print(f"{line:04d} | Running NoYieldListArgs tests...")
for n in range(2000):
    line += 1
    x = NoYieldListArgs(*default_args)
    try:
        assert not isiterable(x)
    except AssertionError:
        print(f"{line:04d} | Test NoYieldListArgs ({n}) failed")
        raise SystemExit
    print(f"{line:04d} | Test NoYieldListArgs ({n}) passed")

# ============= InvalidIterator =============
line += 1
print(f"{line:04d} | Running NoYieldListArgs tests...")
for n in range(2000):
    line += 1
    x = InvalidIterator()
    try:
        assert not isiterable(x)
    except AssertionError:
        print(f"{line:04d} | Test InvalidIterator ({n}) failed")
        raise SystemExit
    print(f"{line:04d} | Test InvalidIterator ({n}) passed")

# ============= InvalidIterator =============
line += 1
print(f"{line:04d} | Running WithoutInitializationIterator tests...")
for n in range(2000):
    line += 1
    x = WithoutInitializationIterator
    try:
        assert not isiterable(x)
    except AssertionError:
        print(f"{line:04d} | Test WithoutInitializationIterator ({n}) failed")
        raise SystemExit
    print(f"{line:04d} | Test WithoutInitializationIterator ({n}) passed")
print("\nDone! The tests were successfully passed.")
