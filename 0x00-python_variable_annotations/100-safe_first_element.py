#!/usr/bin/env python3
'''
unknown input types
'''
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    returns either any type or none
    '''
    if lst:
        return lst[0]
    else:
        return None
