from dataclasses import dataclass
from typing import Type

from ..math.color import Color
from ..raycasthit import RaycastHit
from .shader import Shader, Callback


def get_shader(name: str) -> Type[Shader]:
    return globals()[name.capitalize()]


@dataclass
class Unlit(Shader):
    color: Color

    def evaluate(self, hit: RaycastHit, callback: Callback) -> None:
        callback(self.color)
