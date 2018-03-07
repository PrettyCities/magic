import copy
import re
from typing import Mapping
from typing import Tuple
from typing import TypeVar

from manacosts.basiccost import BasicCost
from manacosts.exceptions import ManaCostParseException
from manacosts.phyrexian import Phyrexian
from manacosts.splitcost import SplitCost
from manacosts.x import X

CostMappingTypes = TypeVar('CostMappingTypes', int, str)


class ManaCostReader(object):
    _KNOWN_TYPES = [BasicCost, SplitCost, Phyrexian, X]

    @classmethod
    def read(cls, cost: str):
        costs = re.findall(r"\{([A-Za-z0-9/*]*)\}", cost)
        counted_costs = {}
        for indv_cost in costs:
            counted_costs = cls._count_cost(counted_costs, cls.parse(indv_cost))
        return counted_costs

    @classmethod
    def parse(cls, individual_cost: str) -> Tuple[str, int]:
        for known_type in cls._KNOWN_TYPES:
            try:
                return known_type.parse(individual_cost)
            except ManaCostParseException:
                continue
        raise ManaCostParseException("No known ManaCost can parse this cost: {}".format(individual_cost))

    @classmethod
    def _count_cost(cls, counted_costs: dict, individual_cost: Tuple[str, int]) -> Mapping[CostMappingTypes, int]:
        cc_copy = copy.deepcopy(counted_costs)
        key = individual_cost[0]
        value = individual_cost[1]
        cc_copy[key] = cc_copy.get(key, 0) + value
        return cc_copy

    @classmethod
    def _extract_cost_type(cls, individual_cost: str):
        pass
