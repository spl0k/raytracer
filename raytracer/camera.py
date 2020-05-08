from .object import Object
from .math.vector import Vector3
from .math.quaternion import Quaternion


class Camera(Object):
    vfov: float

    def __init__(self, pos: Vector3, rot: Quaternion, vfov: float) -> None:
        super().__init__(pos, rot, Vector3(1, 1, 1))
        self.vfov = vfov
