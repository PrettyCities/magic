from typing import Any
from typing import Mapping

from attributes.attribute import Attribute


class ManaType(Attribute):
    def __init__(self, projection: Mapping[str, Any]):
        super().__init__(projection)

    @classmethod
    def Swamp(cls):
        return ManaType(cls._construct_projection("Black"))

    @classmethod
    def _construct_projection(cls, manatype: str):
        return {
            "$project": {
                "cards": {
                    "$filter": {
                        "input": "$cards",
                        "as": "card",
                        "cond": {
                            "$and": [
                                {"$ifNull": ["$$card.colors", False]},
                                # Can't use $in until Mongo 3.4
                                # "$in": [manatype, "$$card.colors"]
                                {"$setIsSubset": [[manatype], "$$card.colors"]}
                            ]
                        }
                    }
                }
            }
        }
