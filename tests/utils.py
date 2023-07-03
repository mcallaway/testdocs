"""
Utility functions.
"""

import itertools

def dict_extract(key, var):
    """Recurse through a dictionary 'var' looking for 'key'."""
    if hasattr(var,'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in dict_extract(key, d):
                        yield result

def peek(iterable):
    """Look into an iterable, like a generator, to extract the first item."""
    try:
        first = next(iterable)
    except StopIteration:
        return None
    return first, itertools.chain([first], iterable)

