from typing import Any
from typing import Mapping


class Attribute(object):
    def __init__(self, projection: Mapping[str, Any]):
        self.projection = projection
