__all__ = ["run","sleep"]

from asyncio import run as async_run
from asyncio import sleep as async_sleep

from typing import Awaitable,Callable

def run(func: Callable) -> None:
    """
    Executes the provided main function asynchronously for web environments.

    Args:
        func (func.main): The main func to be executed.
    """
    async_run(func())

def sleep(n: int) -> Awaitable[None]:
    """
    Pauses execution asynchronously for the specified duration.

    Args:
        n (int): The number of seconds to sleep.

    Returns:
        Awaitable[None]: An awaitable object that needs to be awaited to perform the sleep.
    """
    return async_sleep(n)
