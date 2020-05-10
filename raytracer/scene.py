from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING

from .math.color import Color

if TYPE_CHECKING:
    from .camera import Camera
    from .light import Light
    from .renderable.renderable import Renderable


@dataclass
class Scene:
    cameras: List["Camera"]
    lights: List["Light"]
    objects: List["Renderable"]
    background: Color = field(default=Color(0, 0, 0, 1))
    ambient: Color = field(default=Color(0, 0, 0, 1))
