import pytest

from attributes.mana.cmc import ConvertedManaCost
from attributes.mana.types import ManaType
from cardpools.formats import Standard
from deckbuilder import DeckBuilder


def test_deckbuilder_standard_swamp():
    attributes = [
        [ManaType.Swamp()]
    ]

    cursor = DeckBuilder.build(Standard, attributes)
    sets = [doc for doc in cursor]
    assert 7 == len(sets)


def test_deckbuilder_standard_swamp_additional(black_cmcs):
    black_cmcs = [
        {"cost": 1, "expected": 0},
        {"cost": 2, "expected": 7},
        {"cost": 3, "expected": 19}
    ]

    # TODO: Determine which set this is
    for black_cmc in black_cmcs:
        attributes = [
            [ManaType.Swamp(), ConvertedManaCost < black_cmc["cost"]]
        ]

        cursor = DeckBuilder.build(Standard, attributes)
        sets = [doc for doc in cursor]
        assert black_cmc["expected"] == len(sets[0]["cards"])

