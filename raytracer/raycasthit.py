from dataclasses import dataclass
from typing import TYPE_CHECKING

from .math.color import Color
from .math.vector import Vector3
from .renderable.renderable import Renderable


@dataclass
class RaycastHit:
    obj: Renderable
    direction: Vector3
    position: Vector3
    normal: Vector3

    async def get_color(self) -> Color:
        return await self.obj.shader.evaluate(self)
