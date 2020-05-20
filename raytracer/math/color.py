from dataclasses import dataclass, field
from typing import Union


def clamp(v, a, b):
    return max(a, min(b, v))


def clamp01(v):
    return clamp(v, 0, 1)


@dataclass
class Color:
    r: float
    g: float
    b: float
    a: float = field(default=1)

    def as_color24(self):
        return Color24(
            int(clamp01(self.r) * 255),
            int(clamp01(self.g) * 255),
            int(clamp01(self.b) * 255),
        )

    def as_color32(self):
        return Color32(
            int(clamp01(self.r) * 255),
            int(clamp01(self.g) * 255),
            int(clamp01(self.b) * 255),
            int(clamp01(self.a) * 255),
        )

    def __add__(self, other: "Color") -> "Color":
        if not isinstance(other, Color):
            return NotImplemented
        return Color(
            self.r + other.r, self.g + other.g, self.b + other.b, self.a + other.a,
        )

    def __mul__(self, other: Union["Color", float, int]) -> "Color":
        if isinstance(other, (float, int)):
            return Color(self.r * other, self.g * other, self.b * other, self.a * other)
        if isinstance(other, Color):
            return Color(
                self.r * other.r, self.g * other.g, self.b * other.b, self.a * other.a,
            )
        return NotImplemented

    def __rmul__(self, other: Union[float, int]) -> "Color":
        if not isinstance(other, (float, int)):
            return NotImplemented
        return Color(self.r * other, self.g * other, self.b * other, self.a * other)


@dataclass
class Color24:
    r: int
    g: int
    b: int

    def __post_init__(self):
        if not 0 <= self.r < 256:
            raise ValueError(f"r {self.r}")
        if not 0 <= self.g < 256:
            raise ValueError(f"g {self.g}")
        if not 0 <= self.b < 256:
            raise ValueError(f"b {self.b}")


@dataclass
class Color32(Color24):
    a: int

    def __post_init__(self):
        super().__post_init__()
        if not 0 <= self.a < 256:
            raise ValueError(f"a {self.a}")
