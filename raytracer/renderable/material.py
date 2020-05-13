from abc import ABC, abstractmethod
from dataclasses import dataclass, field, InitVar
from typing import Callable, TYPE_CHECKING

from ..math.color import Color

if TYPE_CHECKING:
    from ..raycasthit import RaycastHit


Callback = Callable[[Color], None]


@dataclass
class MaterialProperties:
    color: Color = field(default=Color(1, 1, 1, 1))
    # For potential future use
    albedoMap: None = field(default=None)
    normalMap: None = field(default=None)


class Shader(ABC):
    @abstractmethod
    def evaluate(
        self, props: MaterialProperties, hit: "RaycastHit", callback: Callback
    ) -> None:
        ...


@dataclass
class Material:
    props: MaterialProperties
    shader: Shader

    def evaluate(self, hit: "RaycastHit", callback: Callback) -> None:
        self.shader.evaluate(self.props, hit, callback)
