import asyncio
from typing import List
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    A coroutine that executes async_comprehension 4 times in parallel
    using asyncio.gather
    '''
    start_time = time.time()

    # Run async_comprehension 4 times in parallel
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
