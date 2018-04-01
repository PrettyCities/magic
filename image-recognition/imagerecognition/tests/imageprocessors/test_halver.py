from imageprocessors.halver import ImageHalver
from imageprocessors.saver import Saver


def test_returns_two_images(image):
    result = ImageHalver.process(image)
    assert 2 == len(list(result))


def test_image_is_half_size(image):
    halves = ImageHalver.process(image)
    # TODO: How to test this?
    for halve in halves:
        Saver.process(halve)
