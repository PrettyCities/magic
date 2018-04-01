from pathlib import Path

import pytest
from PIL import Image

from canvases.mtgotradeboard import MtgoTradeBoard
from imageprocessors.exceptions import ImageExhaustedException
from imageprocessors.utils.pixel_utils import PixelUtils
from imageprocessors.utils.pixel_utils import DIRECTIONS


class TestPixelFinder:
    @pytest.fixture
    def blue_images(self, resources_directory: Path):
        utils_path = resources_directory.joinpath("imageprocessors").joinpath("utils")
        return [
            {
                "image": Image.open(utils_path.joinpath("firstblue_1.png")),
                "expected_location": (0, 0),
            },
            {
                "image": Image.open(utils_path.joinpath("lastblue_1.png")),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(utils_path.joinpath("firstblue_2.png")),
                "expected_location": (0, 0),
            },
            {
                "image": Image.open(utils_path.joinpath("lastblue_2.png")),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(utils_path.joinpath("bluefromposting_1.png")),
                "expected_location": (18, 8)
            },
            {
                "image": Image.open(utils_path.joinpath("bluefromposting_2.png")),
                "expected_location": (12, 6)
            }
        ]

    @pytest.fixture
    def white_images(self, resources_directory: Path):
        utils_path = resources_directory.joinpath("imageprocessors").joinpath("utils")
        return [
            {
                "image": Image.open(utils_path.joinpath("firstwhite_1.png")),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(utils_path.joinpath("lastwhite_1.png")),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(utils_path.joinpath("firstwhite_2.png")),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(utils_path.joinpath("lastwhite_2.png")),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(utils_path.joinpath("whitefromposting_1.png")),
                "expected_location": (0, 1)
            }
        ]

    def test_location_of_first_occurence_blue_images(self, blue_images):
        for image_metadata in blue_images:
            print("Testing location_of_first_occurent with input: {}".format(image_metadata))
            result = PixelUtils.location_of_first_occurrence(color=MtgoTradeBoard.BLUE,
                                                                      image=image_metadata["image"],
                                                                      similarity_threshold=2.2)
            assert image_metadata["expected_location"] == result

    def test_location_of_first_occurence_white_images(self, white_images):
        for image_metadata in white_images:
            print("Testing location_of_first_occurent with input: {}".format(image_metadata))
            result = PixelUtils.location_of_first_occurrence(color=MtgoTradeBoard.WHITE,
                                                                      image=image_metadata["image"],
                                                                      similarity_threshold=2.2)
            assert image_metadata["expected_location"] == result

    def test_is_similar(self):
        # TODO: Decide on if we want to use RGB or RGBA (like below)
        tests = [
            {
                "boxone": (10, 10, 10, 10),
                "boxtwo": (10, 10, 10, 10),
                "threshold": 1.0,
                "expected": True
            },
            {
                "boxone": (10, 10, 10, 10),
                "boxtwo": (10, 10, 10, 10),
                "threshold": 0.0,
                "expected": True
            },
            {
                "boxone": (10, 10, 10, 21),
                "boxtwo": (10, 10, 10, 10),
                "threshold": 100.0,
                "expected": False
            },
            {
                "boxone": (10, 10, 10, 20),
                "boxtwo": (10, 10, 10, 10),
                "threshold": 100.0,
                "expected": True
            },
            {
                "boxone": (11, 10, 10, 10),
                "boxtwo": (10, 10, 10, 10),
                "threshold": 10.0,
                "expected": True
            }
        ]

        # TODO: Add tests with specific colors

        for test in tests:
            print("Testing similarity with input: {}".format(test))
            result = PixelUtils.is_similar(pixel_one=test["boxone"], pixel_two=test["boxtwo"],
                                                    similarity_threshold=test["threshold"])
            assert test["expected"] == result

    def test_move_until_no_match(self, resources_directory):
        utils_path = resources_directory.joinpath("imageprocessors").joinpath("utils")
        similarity_threshold = 2.6

        firstblue = Image.open(utils_path.joinpath("firstblue_1.png"))
        with pytest.raises(ImageExhaustedException):
            PixelUtils.move_until_no_match(color=MtgoTradeBoard.BLUE,
                                           image=firstblue,
                                           direction=DIRECTIONS.RIGHT,
                                           similarity_threshold=similarity_threshold)

        bluefromposting = Image.open(utils_path.joinpath("bluefromposting_1.png"))
        with pytest.raises(ImageExhaustedException):
            PixelUtils.move_until_no_match(color=MtgoTradeBoard.BLUE,
                                           image=bluefromposting,
                                           direction=DIRECTIONS.RIGHT,
                                           similarity_threshold=similarity_threshold,
                                           starting_xy_pixels=(18, 8))

        mtgotraderboard = Image.open(utils_path.joinpath("mtgotradeboard.png"))
        mtgotradeboard_expected = 1894
        result = PixelUtils.move_until_no_match(color=MtgoTradeBoard.BLUE,
                                                image=mtgotraderboard,
                                                direction=DIRECTIONS.RIGHT,
                                                similarity_threshold=similarity_threshold,
                                                starting_xy_pixels=(300, 206))
        assert mtgotradeboard_expected == result
