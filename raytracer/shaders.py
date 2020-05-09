from .material import MaterialProperties
from .math.color import Color
from .raycasthit import RaycastHit


def unlit(props: MaterialProperties, hit: RaycastHit) -> Color:
    return props.color
