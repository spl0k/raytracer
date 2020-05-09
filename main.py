import click
import dacite
import yaml

from raytracer import shaders
from raytracer.material import Shader
from raytracer.renderable.renderable import Renderable, find_renderable_type
from raytracer.scene import Scene


@click.command()
@click.argument("infile")
@click.argument("outfile")
def main(infile, outfile):
    with open(infile, "rt") as instream:
        scenedef = yaml.load(instream, Loader=yaml.SafeLoader)

    scene = dacite.from_dict(
        Scene,
        scenedef,
        config=dacite.Config(
            type_hooks={
                Renderable: lambda d: dacite.from_dict(
                    find_renderable_type(d.pop("type")), d
                )
            }
        ),
    )


if __name__ == "__main__":
    main()
