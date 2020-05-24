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

    @property
    def normalized(self):
        sqrlen = self.sqrlength
        if math.isclose(sqrlen, 1):
            return self

        len = math.sqrt(sqrlen)
        return Vector3(self.x / len, self.y / len, self.z / len)

    def __neg__(self) -> "Vector3":
        return Vector3(-self.x, -self.y, -self.z)

    def __add__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3") -> "Vector3":
        if not isinstance(other, Vector3):
            return NotImplemented
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> "Vector3":
        if not isinstance(other, float):
            return NotImplemented
        return Vector3(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    @staticmethod
    def dot(a: "Vector3", b: "Vector3") -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def reflect(dir: "Vector3", normal: "Vector3") -> "Vector3":
        return dir - 2 * Vector3.dot(dir, normal) * normal
