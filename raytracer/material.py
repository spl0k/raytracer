from dataclasses import dataclass, field, InitVar
from typing import Callable, TYPE_CHECKING

from .math.color import Color
from . import shaders

if TYPE_CHECKING:
    from .raycasthit import RaycastHit


@dataclass
class MaterialProperties:
    color: Color = field(default=Color(1, 1, 1, 1))
    # For potential future use
    albedoMap: None = field(default=None)
    normalMap: None = field(default=None)


Callback = Callable[[Color], None]
Shader = Callable[[MaterialProperties, "RaycastHit", Callback], None]


@dataclass
class Material:
    props: MaterialProperties
    shader_name: InitVar[str]
    shader: Shader = None

    def __post_init__(self, shader_name):
        self.shader = shaders.__dict__[shader_name]

    def evaluate(self, hit: "RaycastHit", callback: Callable[[Color], None]) -> None:
        self.shader(self.props, hit, callback)  # type: ignore
