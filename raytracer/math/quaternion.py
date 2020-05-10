import math

from dataclasses import dataclass
from typing import Union, overload

from .vector import Vector3


@dataclass
class Quaternion:
    __slots__ = ("x", "y", "z", "w")

    x: float
    y: float
    z: float
    w: float

    @property
    def euler(self) -> Vector3:
        sinx_cosy = 2 * (self.w * self.x + self.y * self.z)
        cosx_cosy = 1 - 2 * (self.x * self.x + self.y * self.y)
        x = math.atan2(sinx_cosy, cosx_cosy)

        siny = 2 * (self.w * self.y - self.z * self.x)
        if abs(siny) >= 1:
            y = math.copysign(math.pi * 0.5, siny)
        else:
            y = math.asin(siny)

        sinz_cosy = 2 * (self.w * self.z + self.x * self.y)
        cosz_cosy = 1 - 2 * (self.y * self.y + self.z * self.z)
        z = math.atan2(sinz_cosy, cosz_cosy)

        return Vector3(math.degrees(x), math.degrees(y), math.degrees(z))

    @staticmethod
    def from_euler(euler: Vector3) -> "Quaternion":
        euler = Vector3(
            math.radians(euler.x), math.radians(euler.y), math.radians(euler.z)
        )

        cx = math.cos(euler.x * 0.5)
        sx = math.sin(euler.x * 0.5)
        cy = math.cos(euler.y * 0.5)
        sy = math.sin(euler.y * 0.5)
        cz = math.cos(euler.z * 0.5)
        sz = math.sin(euler.z * 0.5)

        w = cx * cy * cz + sx * sy * sz
        x = sx * cy * cz - cx * sy * sz
        y = cx * sy * cz + sx * cy * sz
        z = cx * cy * sz - sx * sy * cz

        return Quaternion(x, y, z, w)

    @property
    def sqrlength(self) -> float:
        return self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2

    @property
    def length(self) -> float:
        return math.sqrt(self.sqrlength)

    @property
    def normalized(self) -> "Quaternion":
        sqrlen = self.sqrlength
        if math.isclose(sqrlen, 1):
            return self

        len = math.sqrt(sqrlen)
        return Quaternion(self.x / len, self.y / len, self.z / len, self.w / len)

    @overload
    def __mul__(self, other: float) -> "Quaternion":
        ...

    @overload
    def __mul__(self, other: "Quaternion") -> "Quaternion":
        ...

    @overload
    def __mul__(self, other: Vector3) -> Vector3:
        ...

    def __mul__(self, other):
        if isinstance(other, float):
            return self.__float_mul(other)
        if isinstance(other, Quaternion):
            return self.__quat_mul(other)
        if isinstance(other, Vector3):
            return self.__vec_mul(other)
        return NotImplemented

    def __float_mul(self, other: float) -> "Quaternion":
        return Quaternion(
            self.x * other, self.y * other, self.z * other, self.w * other
        )

    def __quat_mul(self, other: "Quaternion") -> "Quaternion":
        x = self.w * other.x + other.w * self.x + self.y * other.z - other.y * self.z
        y = self.w * other.y + other.w * self.y + self.z * other.x - other.z * self.x
        z = self.w * other.z + other.w * self.z + self.x * other.y - other.x * self.y
        w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
        return Quaternion(x, y, z, w)

    def __vec_mul(self, other: Vector3) -> Vector3:
        p = self.normalized
        pc = Quaternion(-p.x, -p.y, -p.z, p.w)
        q = Quaternion(other.x, other.y, other.z, 0)
        rv = p * q * pc
        return Vector3(rv.x, rv.y, rv.z)

    def __rmul__(self, other: float) -> "Quaternion":
        return Quaternion(
            self.x * other, self.y * other, self.z * other, self.w * other
        )


identity = Quaternion(0, 0, 0, 1)
