#!/usr/bin/env python3
'''
callable
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    returns a callable func
    '''
    def mut_func(number: float) -> float:
        '''
        returns a multiple of funct and number
        '''
        return number * multiplier
    return mut_func
