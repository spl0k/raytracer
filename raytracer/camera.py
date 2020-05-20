from dataclasses import dataclass, astuple
from PIL import Image
from typing import TYPE_CHECKING

from .math.color import Color
from .math.quaternion import Quaternion
from .math.vector import Vector3
from .object import Object
from .ray import Ray
from .raycaster import Raycaster, Callback
from .raycasthit import RaycastHit


@dataclass
class Camera(Object):
    vfov: float

    def generate_initial_rays(self, width: int, height: int, background: Color) -> None:
        self.image = Image.new("RGB", (width, height), astuple(background.as_color24()))

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
                Raycaster.instance.add_ray(ray, self.__create_callback(x, y))

                hangle += hstep
            vangle += vstep

    def __create_callback(self, x, y) -> Callback:
        def set_color(color: Color) -> None:
            self.image.putpixel((x, y), astuple(color.as_color24()))

        def callback(hit: RaycastHit) -> None:
            hit.obj.shader.evaluate(hit, set_color)

        return callback
