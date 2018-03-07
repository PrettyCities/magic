from typing import Any
from typing import Mapping

from attributes.attribute import Attribute
from attributes.constructedprojection import ConstructedProjection


class _ConvertedManaCost(Attribute):
    def __init__(self, query: Mapping[str, Any] = None):
        super().__init__(query)

    def __lt__(self, other: int):
        projection = {
            "$project": {
                "cards": {
                    "$filter": {
                        "input": "$cards",
                        "as": "card",
                        "cond": {
                            "$lt": ["$$card.cmc", other]
                        }
                    }
                }
            }
        }
        return ConstructedProjection(projection)


ConvertedManaCost = _ConvertedManaCost()
