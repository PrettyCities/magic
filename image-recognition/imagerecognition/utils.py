from typing import Tuple


class BoxFactory:
    @classmethod
    def make(cls, left: int, upper: int, right: int, lower: int) -> Tuple[int, int, int, int]:
        return (left, upper, right, lower)


def percent_difference(nums: Tuple[float, float]) -> float:
    try:
        return ((abs(nums[0] - nums[1])) / nums[1]) * 100.0
    except ZeroDivisionError:
        return 0
