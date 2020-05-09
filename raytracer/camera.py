from dataclasses import dataclass

from .object import Object
from .math.vector import Vector3
from .math.quaternion import Quaternion


@dataclass
class Camera(Object):
    vfov: float
