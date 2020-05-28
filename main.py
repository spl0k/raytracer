import click
import os.path

from asyncio import as_completed, get_event_loop

from raytracer.math.color import Color
from raytracer.raycaster import Raycaster
from raytracer.scene import Scene
from raytracer.sceneloader import load_scene
from raytracer.utils import Stopwatch


@click.command()
@click.argument("infile", type=click.Path(dir_okay=False))
@click.argument("width", type=int)
@click.argument("height", type=int)
@click.argument("outfile", type=click.Path(dir_okay=False))
def main(infile: str, outfile: str, width: int, height: int):
    loop = get_event_loop()
    scene = load_scene(infile)
    caster = Raycaster(loop, scene)
    sw = Stopwatch()

    name, suffix = os.path.splitext(outfile)
    if not suffix:
        suffix = ".png"
    if len(scene.cameras) > 1:
        name_format = f"{name}_{{}}{suffix}"
    else:
        name_format = f"{name}{suffix}"

    with sw:
        loop.run_until_complete(process_cameras(scene, width, height, name_format))
    print(f"Total: {sw.measured:f}")


async def process_cameras(
    scene: Scene, width: int, height: int, name_format: str
) -> None:
    for i, coro in enumerate(
        as_completed(
            map(
                lambda cam: cam.cast_rays(width, height, scene.background),
                scene.cameras,
            )
        )
    ):
        image = await coro
        image.save(name_format.format(i))


if __name__ == "__main__":
    main()
