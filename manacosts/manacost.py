from typing import Tuple


class ManaCost(object):
    @classmethod
    def parse(cls, individual_cost: str) -> Tuple[str, int]:
        raise NotImplementedError
