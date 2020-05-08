from abc import abstractmethod
from typing import Optional

from ..material import Material
from ..object import Object
from ..ray import Ray
from ..raycasthit import RaycastHit


class Renderable(Object):
    material: Material

    @abstractmethod
    def intersects(self, ray: Ray) -> Optional[RaycastHit]:
        pass
