from .renderable.renderable import Renderable
from .math.vector import Vector3


class RaycastHit:
    position: Vector3
    normal: Vector3
    obj: Renderable
