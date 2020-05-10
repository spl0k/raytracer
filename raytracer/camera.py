from dataclasses import dataclass

from .math.quaternion import Quaternion
from .math.vector import Vector3
from .object import Object
from .ray import Ray


@dataclass
class Camera(Object):
    vfov: float

    def generate_initial_rays(self, width: int, height: int) -> None:
        aspect = width / height
        hfov = self.vfov * aspect

        hstep = hfov / width
        vstep = self.vfov / height

        vangle = (-self.vfov + self.vfov / height) * 0.5
        for y in range(height):
            hangle = (-hfov + hfov / width) * 0.5
            for x in range(width):
                ray = Ray(
                    self.position,
                    Quaternion.from_euler(Vector3(vangle, hangle, 0))
                    * self.rotation
                    * Vector3(0, 0, 1),
                )

                hangle += hstep
            vangle += vstep
