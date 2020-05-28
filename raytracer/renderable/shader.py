from abc import ABC, abstractmethod
from typing import Callable, TYPE_CHECKING

from ..math.color import Color

if TYPE_CHECKING:
    from ..raycasthit import RaycastHit


class Shader(ABC):
    @abstractmethod
    async def evaluate(self, hit: "RaycastHit") -> Color:
        ...
