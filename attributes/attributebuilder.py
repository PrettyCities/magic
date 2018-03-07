from typing import List

from attributes.attribute import Attribute


class AttributeBuilder(object):
    def __init__(self, attributes: List[Attribute]):
        self._attributes = attributes

    def build(self) -> Attribute:
        pass