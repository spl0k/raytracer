from typing import Tuple

from .quaternion import Quaternion
from .vector import Vector3


class Matrix3x4:
    def __init__(self) -> None:
        self.__m = [
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0],
        ]

    def __mul__(self, other: Vector3) -> Vector3:
        """ This isn't a real matrix multiplication """

        x = (
            self.__m[0][0] * other.x
            + self.__m[0][1] * other.y
            + self.__m[0][2] * other.z
            + self.__m[0][3]
        )
        y = (
            self.__m[1][0] * other.x
            + self.__m[1][1] * other.y
            + self.__m[1][2] * other.z
            + self.__m[1][3]
        )
        z = (
            self.__m[2][0] * other.x
            + self.__m[2][1] * other.y
            + self.__m[2][2] * other.z
            + self.__m[2][3]
        )
        return Vector3(x, y, z)

    def mul_dir(self, other: Vector3, keep_length: bool = False) -> Vector3:
        """ Multiplies a direction. Only uses the rotate and scale part of the
        matrix and optionnaly ensure the resulting vector keeps the same length """

        x = (
            self.__m[0][0] * other.x
            + self.__m[0][1] * other.y
            + self.__m[0][2] * other.z
        )
        y = (
            self.__m[1][0] * other.x
            + self.__m[1][1] * other.y
            + self.__m[1][2] * other.z
        )
        z = (
            self.__m[2][0] * other.x
            + self.__m[2][1] * other.y
            + self.__m[2][2] * other.z
        )
        rv = Vector3(x, y, z)

        if keep_length:
            rv = rv.normalized * other.length

        return rv

    @staticmethod
    def trs(t: Vector3, r: Quaternion, s: Vector3) -> "Matrix3x4":
        m = Matrix3x4()
        r = r.normalized

        m.__m[0][0] = (1 - 2 * r.y ** 2 - 2 * r.z ** 2) * s.x
        m.__m[0][1] = (2 * r.z * r.y - 2 * r.z * r.w) * s.y
        m.__m[0][2] = (2 * r.x * r.z + 2 * r.y * r.w) * s.z
        m.__m[0][3] = t.x

        m.__m[1][0] = (2 * r.x * r.y + 2 * r.z * r.w) * s.x
        m.__m[1][1] = (1 - 2 * r.x ** 2 - 2 * r.z ** 2) * s.y
        m.__m[1][2] = (2 * r.y * r.z - 2 * r.x * r.w) * s.y
        m.__m[1][3] = t.y

        m.__m[2][0] = (2 * r.x * r.z - 2 * r.y * r.w) * s.x
        m.__m[2][1] = (2 * r.y * r.z + 2 * r.x * r.w) * s.y
        m.__m[2][2] = (1 - 2 * r.x ** 2 - 2 * r.y ** 2) * s.z
        m.__m[2][3] = t.z

        return m
