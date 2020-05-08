from abc import ABC, abstractmethod

from .math.vector import Vector3
from .math.quaternion import Quaternion


class Object(ABC):
    position: Vector3
    rotation: Quaternion
    scale: Vector3

    @abstractmethod
    def __init__(self, p: Vector3, r: Quaternion, s: Vector3) -> None:
        self.position = p
        self.rotation = r
        self.scale = s
