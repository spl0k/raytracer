from dataclasses import dataclass

from .math.vector import Vector3


@dataclass
class RaycastHit:
    position: Vector3
    normal: Vector3
