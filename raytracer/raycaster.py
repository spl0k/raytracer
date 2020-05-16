import math

from typing import Callable, List, Optional, Tuple

from .ray import Ray
from .raycasthit import RaycastHit
from .scene import Scene
from .utils import Stopwatch

Callback = Callable[[RaycastHit], None]


class Raycaster:
    class Statistics:
        def __init__(self) -> None:
            self.count = 0
            self.total = 0.0
            self.min = math.inf
            self.max = 0.0

        def add_ray(self, duration: float) -> None:
            self.count += 1
            self.total += duration
            self.min = min(self.min, duration)
            self.max = max(self.max, duration)

        def __str__(self) -> str:
            return f"{self.count} rays in {self.total:f}s (min: {self.min:f}s, max: {self.max:f}s, avg: {self.total / self.count:f}s)"

    def __init__(self, scene: Scene) -> None:
        self.__to_process: List[Tuple[Ray, Callback]] = []
        self.__scene = scene
        self.__stats = Raycaster.Statistics()

    @property
    def stats(self):
        return self.__stats

    def add_ray(self, ray: Ray, callback: Callback) -> None:
        self.__to_process.append((ray, callback))

    def process(self) -> None:
        sw = Stopwatch()

        while self.__to_process:
            ray, callback = self.__to_process.pop()
            closest_hit: Tuple[float, Optional[RaycastHit]] = (math.inf, None)

            with sw:
                for o in self.__scene.objects:
                    hit = o.intersects(ray)
                    if hit is not None:
                        closest_hit = min(
                            closest_hit, ((ray.origin - hit.position).sqrlength, hit)
                        )

                if closest_hit[1] is not None:
                    callback(closest_hit[1])

            self.__stats.add_ray(sw.measured)
