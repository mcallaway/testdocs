"""
This is the site module.

The purpose here is to use impement site as a
dataclass so as to have validation.
"""

from dataclasses import dataclass

@dataclass
class Site:

    name: str
