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

    def __add__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
