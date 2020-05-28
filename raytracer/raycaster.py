import math

from asyncio import as_completed
from concurrent.futures import ProcessPoolExecutor
from typing import Awaitable, Dict, List, Optional, Tuple, TYPE_CHECKING

from .math.color import Color
from .math.vector import Vector3
from .ray import Ray
from .raycasthit import RaycastHit
from .utils import add_results

if TYPE_CHECKING:
    from asyncio.events import AbstractEventLoop

    from .light import Light
    from .renderable.renderable import Renderable
    from .scene import Scene

# list of (color, dir) where dir can be None for the ambient
LightsResult = List[Tuple[Color, Optional[Vector3]]]


def _process_ray(ray: Ray, objects: List["Renderable"]) -> Optional[RaycastHit]:
    closest_hit: Tuple[float, Optional[RaycastHit]] = (math.inf, None)

    for o in objects:
        hit = o.intersects(ray)
        if hit is not None:
            closest_hit = min(
                closest_hit, ((ray.origin - hit.position).sqrlength, hit),
            )

    return closest_hit[1]


class Raycaster:
    instance: "Raycaster" = None  # type: ignore

    def __init__(self, loop: "AbstractEventLoop", scene: "Scene") -> None:
        self.__loop = loop
        self.__exctor = ProcessPoolExecutor()
        self.__scene = scene

        Raycaster.instance = self

    async def cast_ray(self, ray: Ray) -> Optional[RaycastHit]:
        return await self.__loop.run_in_executor(
            self.__exctor, _process_ray, ray, self.__scene.objects
        )

    async def get_lights_from(self, pos: Vector3) -> LightsResult:
        results: LightsResult = [(self.__scene.ambient, None)]

        coros: List[Awaitable[Tuple[Optional[RaycastHit], "Light"]]] = []
        for light in self.__scene.lights:
            dir = (light.position - pos).normalized
            coros.append(add_results(self.cast_ray(Ray(pos, dir)), light))
        for coro in as_completed(coros):
            hit, light = await coro

            dir = pos - light.position  # from light to object to be used in results
            if hit is None or (pos - hit.position).sqrlength > dir.sqrlength:
                results.append((light.color, dir.normalized))

        return results
