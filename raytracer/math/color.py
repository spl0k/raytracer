from dataclasses import dataclass, field


@dataclass
class Color:
    r: float
    g: float
    b: float
    a: float = field(default=1)
