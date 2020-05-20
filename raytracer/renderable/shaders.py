from dataclasses import dataclass
from typing import Type

from ..math.color import Color
from ..math.vector import Vector3
from ..raycaster import Raycaster, LightCBParam
from ..raycasthit import RaycastHit
from .shader import Shader, Callback


def get_shader(name: str) -> Type[Shader]:
    return globals()[name.capitalize()]


@dataclass
class Unlit(Shader):
    color: Color

    def evaluate(self, hit: RaycastHit, callback: Callback) -> None:
        callback(self.color)


@dataclass
class Lambert(Shader):
    color: Color

    def evaluate(self, hit: RaycastHit, callback: Callback) -> None:
        def got_lights(lights: LightCBParam) -> None:
            rv = Color(0, 0, 0)
            for color, dir in lights:
                if dir is None:
                    ndl = 1.0
                else:
                    ndl = max(0, Vector3.dot(hit.normal, -dir))
                rv += color * self.color * ndl

            callback(rv)

        Raycaster.instance.get_lights_from(
            hit.position + hit.normal * 0.000001, got_lights
        )
