from asyncio import as_completed
from dataclasses import dataclass, astuple
from PIL import Image
from typing import Awaitable, List, Optional, Tuple

from .math.color import Color
from .math.quaternion import Quaternion
from .math.vector import Vector3
from .object import Object
from .ray import Ray
from .raycaster import Raycaster
from .raycasthit import RaycastHit
from .utils import add_results


@dataclass
class Camera(Object):
    vfov: float

    async def cast_rays(
        self, width: int, height: int, background: Color
    ) -> Image.Image:
        image = Image.new("RGB", (width, height), astuple(background.as_color24()))

        aspect = width / height
        hfov = self.vfov * aspect

        hstep = hfov / width
        vstep = self.vfov / height

        raycoros: List[Awaitable[Tuple[Optional[RaycastHit], Tuple[int, int]]]] = []
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
                raycoros.append(add_results(Raycaster.instance.cast_ray(ray), (x, y)))

                hangle += hstep
            vangle += vstep

        shadercoros: List[Awaitable[Tuple[Color, Tuple[int, int]]]] = []
        for rc in as_completed(raycoros):
            hit, pos = await rc
            if hit is not None:
                shadercoros.append(add_results(hit.get_color(), pos))

        for sc in as_completed(shadercoros):
            color, (x, y) = await sc
            image.putpixel((x, y), astuple(color.as_color24()))

        return image
