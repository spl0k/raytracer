import math

from dataclasses import dataclass


@dataclass
class Vector2:
    __slots__ = ("x", "y")

    x: float
    y: float

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @property
    def sqrlength(self) -> float:
        return self.x ** 2 + self.y ** 2

    @property
    def length(self) -> float:
        return math.sqrt(self.sqrlength)


@dataclass
class Vector3:
    __slots__ = ("x", "y", "z")

    x: float
    y: float
    z: float

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    @property
    def sqrlength(self) -> float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    @property
    def length(self) -> float:
        return math.sqrt(self.sqrlength)
