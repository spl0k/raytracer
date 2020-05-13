import importlib

from abc import abstractmethod
from dataclasses import dataclass
from typing import Optional, Type, TYPE_CHECKING

from ..object import Object

if TYPE_CHECKING:
    from ..ray import Ray
    from ..raycasthit import RaycastHit
    from .material import Material


@dataclass
class Renderable(Object):
    material: "Material"

    @abstractmethod
    def intersects(self, ray: "Ray") -> Optional["RaycastHit"]:
        ...


def find_renderable_type(name: str) -> Type[Renderable]:
    m = importlib.import_module(f".{name}", __package__)
    return getattr(m, name[0].upper() + name[1:])
