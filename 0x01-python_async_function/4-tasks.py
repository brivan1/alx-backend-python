#!/usr/bin/env python3
'''
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
'''

import asyncio
from typing import List
import importlib

basic_async_syntax = importlib.import_module('0-basic_async_syntax')
wait_random = getattr(basic_async_syntax, 'wait_random')


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Args:
        max_delay (int): maximum delay time
    Returns:
        asyncio.Task: Task object representing the execution of wait_random
    '''
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Args:
        n (int): number of times to spawn task_wait_random
        max_delay (int): maximum delay time

    Returns:
        List[float]: list of delays in ascending order
    '''
    tasks = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    delays = await asyncio.gather(*tasks)
    delays.sort()

    return delays
