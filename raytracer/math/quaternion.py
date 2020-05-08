import math

from .vector import Vector3


class Quaternion:
    __slots__ = ("x", "y", "z", "w")

    x: float
    y: float
    z: float
    w: float

    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    @property
    def euler(self) -> Vector3:
        sinx = 2 * (self.w * self.y - self.z * self.x)
        if abs(sinx) >= 1:
            x = math.copysign(math.pi * 0.5, sinx)
        else:
            x = math.asin(sinx)

        siny_cosx = 2 * (self.w * self.z + self.x * self.y)
        cosy_cosx = 1 - 2 * (self.y * self.y + self.z * self.z)
        y = math.atan2(siny_cosx, cosy_cosx)

        sinz_cosx = 2 * (self.w * self.x + self.y * self.z)
        cosz_cosx = 1 - 2 * (self.x * self.x + self.y * self.y)
        z = math.atan2(sinz_cosx, cosz_cosx)

        return Vector3(x, y, z)

    @staticmethod
    def from_euler(euler: Vector3) -> "Quaternion":
        cx = math.cos(euler.x * 0.5)
        sx = math.sin(euler.x * 0.5)
        cy = math.cos(euler.y * 0.5)
        sy = math.sin(euler.y * 0.5)
        cz = math.cos(euler.z * 0.5)
        sz = math.sin(euler.z * 0.5)

        w = cz * cx * cy + sz * sx * sy
        x = sz * cx * cy - cz * sx * sy
        y = cz * sx * cy + sz * cx * sy
        z = cz * cx * sy - sz * sx * cy

        return Quaternion(x, y, z, w)
