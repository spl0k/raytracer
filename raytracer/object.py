from abc import ABC
from dataclasses import dataclass
from functools import cached_property

from .math.matrix import Matrix3x4
from .math.quaternion import Quaternion
from .math.vector import Vector3


@dataclass
class Object(ABC):
    position: Vector3
    rotation: Quaternion
    scale: Vector3

    @cached_property
    def local_to_world_matrix(self) -> Matrix3x4:
        return Matrix3x4.trs(self.position, self.rotation, self.scale)

    @cached_property
    def world_to_local_matrix(self) -> Matrix3x4:
        return Matrix3x4.trs(
            -self.position,
            self.rotation.conjugate,
            Vector3(1 / self.scale.x, 1 / self.scale.y, 1 / self.scale.z),
        )
