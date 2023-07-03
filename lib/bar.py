"""
This is the bar module.

The purpose here is to use impement bar as a
dataclass so as to have validation.
"""

from dataclasses import dataclass

@dataclass
class Bar:

    name: str
    dont_be_missing: str
