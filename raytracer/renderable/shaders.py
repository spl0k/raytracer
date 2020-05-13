from typing import Callable

from ..math.color import Color
from ..raycasthit import RaycastHit
from .material import MaterialProperties, Shader, Callback

ShaderLike = Callable[[MaterialProperties, RaycastHit, Callback], None]


class as_shader(Shader):
    def __init__(self, func: ShaderLike) -> None:
        self.func = func

    def evaluate(
        self, props: MaterialProperties, hit: RaycastHit, callback: Callback
    ) -> None:
        self.func(props, hit, callback)


def get_shader(name: str) -> Shader:
    return globals()[name]


@as_shader
def unlit(props: MaterialProperties, hit: RaycastHit, callback: Callback) -> None:
    callback(props.color)
