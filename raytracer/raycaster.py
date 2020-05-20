import math

from dataclasses import dataclass
from typing import Callable, List, Optional, Tuple, TYPE_CHECKING

from .math.color import Color
from .math.vector import Vector3
from .ray import Ray
from .raycasthit import RaycastHit
from .utils import Stopwatch

if TYPE_CHECKING:
    from .scene import Scene

Callback = Callable[[RaycastHit], None]
NoneCallback = Callable[[], None]

# list of (color, dir) where dir can be None for the ambient
LightCBParam = List[Tuple[Color, Optional[Vector3]]]
LightsCallback = Callable[[LightCBParam], None]


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

    @dataclass
    class Data:
        ray: Ray
        hit_callback: Callback
        none_callback: Optional[NoneCallback]

    instance: "Raycaster" = None

    def __init__(self, scene: "Scene") -> None:
        self.__to_process: List[Raycaster.Data] = []
        self.__scene = scene
        self.__stats = Raycaster.Statistics()

        Raycaster.instance = self

    @property
    def stats(self):
        return self.__stats

    def add_ray(
        self, ray: Ray, callback: Callback, none_cb: Optional[NoneCallback] = None
    ) -> None:
        self.__to_process.append(Raycaster.Data(ray, callback, none_cb))

    def process(self) -> None:
        sw = Stopwatch()

        while self.__to_process:
            data = self.__to_process.pop()
            closest_hit: Tuple[float, Optional[RaycastHit]] = (math.inf, None)

            with sw:
                for o in self.__scene.objects:
                    hit = o.intersects(data.ray)
                    if hit is not None:
                        closest_hit = min(
                            closest_hit,
                            ((data.ray.origin - hit.position).sqrlength, hit),
                        )

                if closest_hit[1] is not None:
                    data.hit_callback(closest_hit[1])
                elif data.none_callback is not None:
                    data.none_callback()

            self.__stats.add_ray(sw.measured)

    def get_lights_from(self, pos: Vector3, callback: LightsCallback) -> None:
        count = len(self.__scene.lights)
        results: LightCBParam = [(self.__scene.ambient, None)]
        processed = 0

        def make_cb(color: Color, dir: Vector3) -> Callback:
            def func(hit: RaycastHit) -> None:
                nonlocal processed

                if (pos - hit.position).sqrlength > dir.sqrlength:
                    results.append((color, dir.normalized))

                processed += 1
                if processed == count:
                    callback(results)

            return func

        def make_none_cb(color: Color, dir: Vector3) -> NoneCallback:
            def func() -> None:
                nonlocal processed

                results.append((color, dir.normalized))

                processed += 1
                if processed == count:
                    callback(results)

            return func

        if not self.__scene.lights:
            callback(results)
            return

        for light in self.__scene.lights:
            dir = pos - light.position  # from light to object to be used in callback
            self.add_ray(
                Ray(pos, -dir.normalized),
                make_cb(light.color, dir),
                make_none_cb(light.color, dir),
            )
