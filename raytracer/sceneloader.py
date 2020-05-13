import dacite
import yaml

from .camera import Camera
from .light import Light
from .math.quaternion import Quaternion
from .math.vector import Vector3
from .raycasthit import RaycastHit
from .renderable.material import Material, Shader
from .renderable.renderable import Renderable, find_renderable_type
from .renderable.shaders import get_shader
from .scene import Scene


def load_renderable(dict: dict) -> Renderable:
    type = dict.pop("type")
    return dacite.from_dict(find_renderable_type(type), dict, config=config)


config = dacite.Config(
    forward_references={
        "Camera": Camera,
        "Light": Light,
        "Material": Material,
        "RaycastHit": RaycastHit,
        "Renderable": Renderable,
    },
    type_hooks={
        Renderable: load_renderable,
        Quaternion: lambda d: Quaternion.from_euler(Vector3(**d)),
        Shader: get_shader,
    },
)


def load_scene(path: str) -> Scene:
    with open(path, "rt") as stream:
        scenedef = yaml.load(stream, Loader=yaml.SafeLoader)

    return dacite.from_dict(Scene, scenedef, config=config)
