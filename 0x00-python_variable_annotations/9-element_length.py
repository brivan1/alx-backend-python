i#!/usr/bin/env python3
"""
fixing some annotation
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    return a list
    '''
    return [(i, len(i)) for i in lst]
