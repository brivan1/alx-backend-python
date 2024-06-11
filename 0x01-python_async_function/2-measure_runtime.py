#!/usr/bin/env python3
'''
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.
'''
import time
import asyncio
import importlib

concurrent_coroutine = importlib.import_module('1-concurrent_coroutines')
wait_n = getattr(concurrent_coroutine, 'wait_n')


def measure_time(n: int, max_delay: int) -> float:
    '''
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): maximum delay time
    Returns:
        float: average execution time for wait_n(n, max_delay)
    '''
    async def async_measure_time():
        start_time = time.perf_counter()
        await wait_n(n, max_delay)
        end_time = time.perf_counter()
        return (end_time - start_time) / n

    return asyncio.run(async_measure_time())
