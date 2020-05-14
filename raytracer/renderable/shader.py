from abc import ABC, abstractmethod
from typing import Callable, TYPE_CHECKING

from ..math.color import Color

if TYPE_CHECKING:
    from ..raycasthit import RaycastHit

Callback = Callable[[Color], None]


class Shader(ABC):
    @abstractmethod
    def evaluate(self, hit: "RaycastHit", callback: Callback) -> None:
        ...
