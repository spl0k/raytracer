from typing import Optional

from ..math.vector import Vector3
from ..ray import Ray
from ..raycasthit import RaycastHit
from .renderable import Renderable


class Plane(Renderable):
    """ XZ-aligned plane, normal pointing towards Y+ """

    def intersects(self, ray: Ray) -> Optional[RaycastHit]:
        w2l = self.world_to_local_matrix
        o = w2l * ray.origin
        d = w2l.mul_dir(ray.direction, True)
        n = Vector3(0, 1, 0)

        dot = Vector3.dot(n, d)
        if abs(dot) > 0.000001:
            t = Vector3.dot(-o, n) / dot
            if t >= 0.000001:
                l2w = self.local_to_world_matrix
                return RaycastHit(
                    self, ray.direction, l2w * (o + d * t), l2w.mul_dir(n, True)
                )

        return None
