from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional

from ..material import Material
from ..object import Object
from ..ray import Ray
from ..raycasthit import RaycastHit


@dataclass
class Renderable(Object):
    material: Material

    @abstractmethod
    def intersects(self, ray: Ray) -> Optional[RaycastHit]:
        ...
