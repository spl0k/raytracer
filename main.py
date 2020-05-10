import click
import dacite
import yaml

from raytracer import shaders
from raytracer.camera import Camera
from raytracer.light import Light
from raytracer.material import Material, Shader
from raytracer.math.quaternion import Quaternion
from raytracer.math.vector import Vector3
from raytracer.raycasthit import RaycastHit
from raytracer.renderable.renderable import Renderable, find_renderable_type
from raytracer.scene import Scene


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
    },
)


@click.command()
@click.argument("infile", type=click.Path(dir_okay=False))
@click.argument("width", type=int)
@click.argument("height", type=int)
@click.argument("outfile")
def main(infile, outfile, width, height):
    with open(infile, "rt") as instream:
        scenedef = yaml.load(instream, Loader=yaml.SafeLoader)

    scene = dacite.from_dict(Scene, scenedef, config=config)
    for cam in scene.cameras:
        cam.generate_initial_rays(width, height)


if __name__ == "__main__":
    main()
