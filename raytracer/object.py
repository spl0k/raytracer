from abc import ABC
from dataclasses import dataclass
from typing import Optional, Union

from .math.vector import Vector3
from .math.quaternion import Quaternion, identity


@dataclass
class Object(ABC):
    position: Vector3
    rotation: Union[Quaternion, Vector3, None]
    scale: Optional[Vector3]

    def __post_init__(self):
        # Default values without using dataclasses.field(default=...) as this
        # would cause issues with fields from inherited class without a default

        if self.rotation is None:
            self.rotation = identity
        elif isinstance(self.rotation, Vector3):
            self.rotation = Quaternion.from_euler(self.rotation)

        if self.scale is None:
            self.scale = Vector3(1, 1, 1)
