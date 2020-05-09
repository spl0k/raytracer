import importlib

from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional, Type

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


def find_renderable_type(name: str) -> Type[Renderable]:
    m = importlib.import_module(f".{name}", __package__)
    return m.__dict__[name[0].upper() + name[1:]]
