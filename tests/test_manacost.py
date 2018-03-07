from manacosts.manacostreader import ManaCostReader


def test_read():
    costs = [
        {"provided": "{8}{G}{G}", "expected": {"colorless": 8, "forest": 2}},
        {"provided": "{2}{G/U}{W}", "expected": {"colorless": 2, "plains": 1, "forest/island": 1}},
        {"provided": "{X}{W}{W}{B}{B}", "expected": {"plains": 2, "swamp": 2, "X": 1}},
        {"provided": "{X}{X}{B}{B}{B}{B}", "expected": {"swamp": 4, "X": 2}},
        {"provided": "{4}{G/P}{G/P}", "expected": {"colorless": 4, "forest/phyrexian": 2}}
    ]

    for cost in costs:
        result = ManaCostReader.read(cost=cost["provided"])
        assert cost["expected"] == result
