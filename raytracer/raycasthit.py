from dataclasses import dataclass
from typing import TYPE_CHECKING

from .math.vector import Vector3
from .renderable.renderable import Renderable


@dataclass
class RaycastHit:
    obj: Renderable
    position: Vector3
    normal: Vector3
