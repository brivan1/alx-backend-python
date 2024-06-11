#!/usr/bin/env python3
'''
Import wait_random from 0-basic_async_syntax.
Write a function (do not create an async function,
use the regular function syntax to do this) task_wait_random
that takes an integer max_delay and returns a asyncio.Task.
'''

import asyncio
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
