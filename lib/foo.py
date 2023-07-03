"""
This is the foo module.

The purpose here is to use impement foo as a
dataclass so as to have validation.
"""

from dataclasses import dataclass

@dataclass
class Foo:

    name: str
