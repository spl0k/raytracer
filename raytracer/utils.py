import time


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
