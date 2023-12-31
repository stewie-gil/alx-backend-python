#!/usr/bin/env python3
"""This module contains an asynchronous coroutine """


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measuring the run time"""
    start_time: float = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time: float = time.time()

    elapsed_time = end_time - start_time
    return elapsed_time/n
