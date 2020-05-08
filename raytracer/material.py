from typing import Callable

from .math.color import Color
from .raycasthit import RaycastHit


class MaterialProperties:
    color: Color
    # For potential future use
    albedoMap: None
    normalMap: None


Shader = Callable[[MaterialProperties, RaycastHit], Color]


class Material:
    shader: Shader
    props: MaterialProperties
