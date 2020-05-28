import time

from typing import Any, Awaitable, Tuple, TypeVar

T = TypeVar("T")
U = TypeVar("U")


async def add_results(awaitable: Awaitable[T], arg: U) -> Tuple[T, U]:
    return (await awaitable, arg)


class Stopwatch:
    def __init__(self):
        self.__start = None
        self.__end = None

    @property
    def measured(self) -> float:
        if self.__start is None:
            raise ValueError("Stopwatch hasn't been started")
        if self.__end is None:
            raise ValueError("Stopwatch is running")

        return self.__end - self.__start

    def __enter__(self):
        self.__start = time.monotonic()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__end = time.monotonic()
