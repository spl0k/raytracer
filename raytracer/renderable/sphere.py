from math import sqrt
from typing import Optional

from ..math.vector import Vector3
from ..ray import Ray
from ..raycasthit import RaycastHit
from .renderable import Renderable


class Sphere(Renderable):
    """ Unit radius sphere. Change its scale to act on its radius """

    def intersects(self, ray: Ray) -> Optional[RaycastHit]:
        w2l = self.world_to_local_matrix
        o = -(w2l * ray.origin)
        d = (w2l * ray.direction).normalized

        t = Vector3.dot(o, d)
        if t < 0.0:
            return None

        d2 = o.sqrlength - t ** 2
        if d2 > 1.0:  # 1 = 1 * 1 = radius * radius
            return None

        pos = -o + d * (t - sqrt(1 - d2))

        l2w = self.local_to_world_matrix
        return RaycastHit(self, l2w * pos, (l2w * pos).normalized)
