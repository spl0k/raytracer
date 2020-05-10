from abc import ABC
from dataclasses import dataclass

from .math.vector import Vector3
from .math.quaternion import Quaternion


@dataclass
class Object(ABC):
    position: Vector3
    rotation: Quaternion
    scale: Vector3
