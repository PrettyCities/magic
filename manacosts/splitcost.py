from typing import Tuple

from manacosts.exceptions import ManaCostParseException
from manacosts.basiccost import BasicCost
from manacosts.manacost import ManaCost


class SplitCost(ManaCost):
    @classmethod
    def parse(cls, individual_cost: str) -> Tuple[str, int]:
        # TODO: Consider how best to handle these costs
        if "/" not in individual_cost:
            raise ManaCostParseException
        else:
            key = cls._extract_colors(individual_cost)
            value = 1

        return key, value

    @classmethod
    def _extract_colors(cls, individual_cost: str) -> str:
        colors = individual_cost.split("/")
        try:
            extracted_colors = "/".join([
                BasicCost.COST_MAPPINGS[color] for color in colors
            ])
        except KeyError:
            raise ManaCostParseException

        return extracted_colors
