from typing import Tuple

from manacosts.exceptions import ManaCostParseException
from manacosts.manacost import ManaCost


class X(ManaCost):
    COST_MAPPINGS = {"X": "X"}

    @classmethod
    def parse(cls, individual_cost: str) -> Tuple[str, int]:
        try:
            key = cls.COST_MAPPINGS[individual_cost]
        except KeyError:
            raise ManaCostParseException
        else:
            value = 1

        return key, value
