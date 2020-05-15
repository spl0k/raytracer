from math import sqrt
from typing import Optional

from ..math.vector import Vector3
from ..ray import Ray
from ..raycasthit import RaycastHit
from .renderable import Renderable


class Sphere(Renderable):
    """ Unit radius sphere. Change its scale to act on its radius """

    def intersects(self, ray: Ray) -> Optional[RaycastHit]:
        l = self.position - ray.origin
        t = Vector3.dot(l, ray.direction)
        if t < 0.0:
            return None

        d2 = l.sqrlength - t ** 2
        if d2 > 1.0:  # 1 = 1 * 1 = radius * radius
            return None

        pos = ray.origin + ray.direction * (t - sqrt(1 - d2))
        n = (pos - self.position).normalized
        return RaycastHit(self, pos, n)
