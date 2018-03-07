from typing import Mapping

from attributes.attribute import Attribute


class GenericAttribute(Attribute):
    def __init__(self, query: Mapping[str, str] = None):
        super(GenericAttribute).__init__(query)