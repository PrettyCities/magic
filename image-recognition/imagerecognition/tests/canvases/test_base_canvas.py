from canvases.base import BaseCanvas


def test_is_viewable(image):
    canvas = BaseCanvas(image=image)
    assert canvas.view() == image
