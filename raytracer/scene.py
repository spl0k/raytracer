from typing import List

from .camera import Camera
from .light import Light
from .math.color import Color
from .renderable.renderable import Renderable


class Scene:
    background: Color
    ambient: Color
    cameras: List[Camera]
    lights: List[Light]
    objects: List[Renderable]
