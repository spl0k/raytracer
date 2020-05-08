import math


class Vector2:
    __slots__ = ("x", "y")

    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @property
    def sqrlength(self) -> float:
        return self.x ** 2 + self.y ** 2

    @property
    def length(self) -> float:
        return math.sqrt(self.sqrlength)


class Vector3:
    __slots__ = ("x", "y", "z")

    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    @property
    def sqrlength(self) -> float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    @property
    def length(self) -> float:
        return math.sqrt(self.sqrlength)
