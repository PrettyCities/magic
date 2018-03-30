from resources import Resources

from imageprocessors.utils import ImageProcessorUtils
from imageprocessors.utils import DIRECTIONS


def test_location_of_first_occurence():
    for image_metadata in Resources.blue_images():
        print("Testing location_of_first_occurent with input: {}".format(image_metadata))
        result = ImageProcessorUtils.location_of_first_occurrence(color=Resources.COLORS["blue"],
                                                                  image=image_metadata["image"],
                                                                  similarity_threshold=2.2)
        assert image_metadata["expected_location"] == result

    for image_metadata in Resources.white_images():
        print("Testing location_of_first_occurent with input: {}".format(image_metadata))
        result = ImageProcessorUtils.location_of_first_occurrence(color=Resources.COLORS["white"],
                                                                  image=image_metadata["image"],
                                                                  similarity_threshold=2.2)
        assert image_metadata["expected_location"] == result


def test_is_similar():
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
        result = ImageProcessorUtils.is_similar(pixel_one=test["boxone"], pixel_two=test["boxtwo"],
                                                similarity_threshold=test["threshold"])
        assert test["expected"] == result


def test_move_until_no_match():
    similarity_threshold = 2.6

    firstblue_1_expected = None
    result_1 = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["blue"],
                                                       image=Resources.firstblue_1(),
                                                       direction=DIRECTIONS.RIGHT,
                                                       similarity_threshold=similarity_threshold)
    assert firstblue_1_expected == result_1

    bluefromposting_1_expected = None
    result_2 = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["blue"],
                                                       image=Resources.bluefromposting_1(),
                                                       direction=DIRECTIONS.RIGHT,
                                                       similarity_threshold=similarity_threshold,
                                                       starting_xy_pixels=(18, 8))
    assert bluefromposting_1_expected == result_2

    mtgotradeboard_expected = 1894
    result_3 = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["blue"],
                                                       image=Resources.mtgotraderboard(),
                                                       direction=DIRECTIONS.RIGHT,
                                                       similarity_threshold=similarity_threshold,
                                                       starting_xy_pixels=(300, 206))
    assert mtgotradeboard_expected == result_3
