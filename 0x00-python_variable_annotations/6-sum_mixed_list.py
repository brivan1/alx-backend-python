'''
module for returning floats
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    takes in mixed list sums and returns float
    '''
    return float(sum(mxd_lst))
