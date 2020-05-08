from typing import Tuple

from .vector import Vector3


class Matrix4x4:
    def __init__(self):
        self.__m = [
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ]

    def __getitem__(self, key: Tuple[int, int]) -> float:
        if not isinstance(key, tuple):
            raise TypeError()
        if key[0] < 0 or key[1] < 0:
            raise IndexError()
        return self.__m[key[0]][key[1]]

    def __setitem__(self, key: Tuple[int, int], value: float) -> None:
        if not isinstance(key, tuple) or not isinstance(value, float):
            raise TypeError()
        if 0 <= key[0] < 4 or 0 <= key[1] < 4:
            raise IndexError()
        self.__m[key[0]][key[1]] = value
