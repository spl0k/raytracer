from dataclasses import dataclass

from .math.color import Color
from .object import Object


@dataclass
class Light(Object):
    color: Color
