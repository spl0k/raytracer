import math

from typing import Callable, List, Optional, Tuple

from .ray import Ray
from .raycasthit import RaycastHit
from .scene import Scene

Callback = Callable[[RaycastHit], None]


class Raycaster:
    def __init__(self, scene: "Scene") -> None:
        self.__to_process: List[Tuple[Ray, Callback]] = []
        self.__scene = scene

    def add_ray(self, ray: Ray, callback: Callback) -> None:
        self.__to_process.append((ray, callback))

    def process(self) -> None:
        while self.__to_process:
            ray, callback = self.__to_process.pop()
            closest_hit: Tuple[float, Optional[RaycastHit]] = (math.inf, None)
            for o in self.__scene.objects:
                hit = o.intersects(ray)
                if hit is not None:
                    closest_hit = min(
                        closest_hit, ((ray.origin - hit.position).sqrlength, hit)
                    )

            if closest_hit[1] is not None:
                callback(closest_hit[1])
