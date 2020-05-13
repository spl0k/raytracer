import click

from raytracer.raycaster import Raycaster
from raytracer.sceneloader import load_scene


@click.command()
@click.argument("infile", type=click.Path(dir_okay=False))
@click.argument("width", type=int)
@click.argument("height", type=int)
@click.argument("outfile")
def main(infile: str, outfile: str, width: int, height: int):
    scene = load_scene(infile)
    caster = Raycaster(scene)
    for cam in scene.cameras:
        cam.generate_initial_rays(width, height, caster, scene.background)

    caster.process()


if __name__ == "__main__":
    main()
