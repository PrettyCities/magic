from typing import Tuple

from manacosts.exceptions import ManaCostParseException
from manacosts.manacost import ManaCost


class BasicCost(ManaCost):
    COST_MAPPINGS = {
        int: "colorless",
        "G": "forest",
        "U": "island",
        "B": "swamp",
        "R": "mountain",
        "W": "plains"
    }

    @classmethod
    def parse(cls, individual_cost: str) -> Tuple[str, int]:
        try:
            int(individual_cost)
        except ValueError:
            try:
                key = cls.COST_MAPPINGS[individual_cost]
            except KeyError:
                raise ManaCostParseException
            else:
                value = 1
        else:
            key = cls.COST_MAPPINGS[int]
            value = int(individual_cost)

        return key, value
