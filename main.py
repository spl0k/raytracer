import click
import os.path

from raytracer.raycaster import Raycaster
from raytracer.sceneloader import load_scene
from raytracer.utils import Stopwatch


@click.command()
@click.argument("infile", type=click.Path(dir_okay=False))
@click.argument("width", type=int)
@click.argument("height", type=int)
@click.argument("outfile", type=click.Path(dir_okay=False))
def main(infile: str, outfile: str, width: int, height: int):
    scene = load_scene(infile)
    caster = Raycaster(scene)
    sw = Stopwatch()

    with sw:
        for cam in scene.cameras:
            cam.generate_initial_rays(width, height, caster, scene.background)
    print(f"Initialization: {sw.measured:f}")

    with sw:
        caster.process()
    print(f"Processing: {sw.measured:f}")
    print(caster.stats)

    name, suffix = os.path.splitext(outfile)
    if not suffix:
        suffix = ".png"
    if len(scene.cameras) > 1:
        name_format = f"{name}_{{}}{suffix}"
    else:
        name_format = f"{name}{suffix}"

    with sw:
        for i, cam in enumerate(scene.cameras):
            cam.image.save(name_format.format(i))
    print(f"Writing result images: {sw.measured:f}")


if __name__ == "__main__":
    main()
