from dataclasses import dataclass

from .math.vector import Vector3


@dataclass
class Ray:
    origin: Vector3
    direction: Vector3
