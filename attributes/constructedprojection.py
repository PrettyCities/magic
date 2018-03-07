from typing import Any
from typing import Mapping

from attributes.attribute import Attribute


class ConstructedProjection(Attribute):
    def __init__(self, projection: Mapping[str, Any]):
        super().__init__(projection)
