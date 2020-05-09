from dataclasses import dataclass, field, InitVar
from typing import Callable

from .math.color import Color
from .raycasthit import RaycastHit
from . import shaders


@dataclass
class MaterialProperties:
    color: Color = field(default=Color(1, 1, 1, 1))
    # For potential future use
    albedoMap: None = field(default=None)
    normalMap: None = field(default=None)


Shader = Callable[[MaterialProperties, RaycastHit], Color]


@dataclass
class Material:
    props: MaterialProperties
    shader_name: InitVar[str]
    shader: Shader = None

    def __post_init__(self, shader_name):
        self.shader = shaders.__dict__[shader_name]
