from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Type

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


class LitShader(Shader, ABC):
    @abstractmethod
    def _evaluate_light(
        self, color: Color, dir: Optional[Vector3], hit: RaycastHit
    ) -> Color:
        ...

    def evaluate(self, hit: RaycastHit, callback: Callback) -> None:
        def got_lights(lights: LightCBParam) -> None:
            rv = Color(0, 0, 0)
            for color, dir in lights:
                rv += self._evaluate_light(color, dir, hit)

            callback(rv)

        Raycaster.instance.get_lights_from(
            hit.position + hit.normal * 0.000001, got_lights
        )


@dataclass
class Lambert(LitShader):
    color: Color

    def _evaluate_light(
        self, color: Color, dir: Optional[Vector3], hit: RaycastHit
    ) -> Color:
        if dir is None:
            ndl = 1.0
        else:
            ndl = max(0, Vector3.dot(hit.normal, -dir))
        return color * self.color * ndl


@dataclass
class Phong(LitShader):
    diffuseColor: Color
    specularColor: Color
    shininess: float

    def _evaluate_light(
        self, color: Color, dir: Optional[Vector3], hit: RaycastHit
    ) -> Color:
        if dir is None:
            return color * self.diffuseColor

        ndl = Vector3.dot(hit.normal, -dir)
        if ndl < 0.000001:
            return Color(0, 0, 0)

        diffuse = color * self.diffuseColor * ndl

        r = Vector3.reflect(dir, hit.normal)
        rdv = Vector3.dot(r, -hit.direction)
        if rdv < 0.000001:
            return diffuse

        specPower = rdv ** self.shininess
        specular = color * self.specularColor * specPower

        return diffuse + specular
