from typing import Optional

from ..ray import Ray
from ..raycasthit import RaycastHit
from .renderable import Renderable


class Sphere(Renderable):
    """ Unit sphere. Change its scale to act on its radius """

    def intersects(self, ray: Ray) -> Optional[RaycastHit]:
        raise NotImplementedError()
