from .math.vector import Vector3


class Ray:
    origin: Vector3
    direction: Vector3

    def __init__(self, origin: Vector3, direction: Vector3):
        self.origin = origin
        self.direction = direction
