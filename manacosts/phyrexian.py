from manacosts.basiccost import BasicCost
from manacosts.splitcost import SplitCost


class Phyrexian(SplitCost):
    COST_MAPPINGS = {"P": "phyrexian"}
    COST_MAPPINGS.update(BasicCost.COST_MAPPINGS)

    @classmethod
    def _extract_colors(cls, individual_cost: str) -> str:
        colors = individual_cost.split("/")
        return "/".join([
            cls.COST_MAPPINGS[color] for color in colors
        ])
