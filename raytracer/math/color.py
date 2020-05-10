from dataclasses import dataclass, field


@dataclass
class Color:
    r: float
    g: float
    b: float
    a: float = field(default=1)

    def as_color32(self):
        return Color32(
            int(self.r * 255), int(self.g * 255), int(self.b * 255), int(self.a * 255)
        )


@dataclass
class Color32:
    r: int
    g: int
    b: int
    a: int

    def __post_init__(self):
        if not 0 <= self.r < 256:
            raise ValueError("r")
        if not 0 <= self.g < 256:
            raise ValueError("g")
        if not 0 <= self.b < 256:
            raise ValueError("b")
        if not 0 <= self.a < 256:
            raise ValueError("a")
