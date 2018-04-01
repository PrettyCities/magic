from canvases.screenshot import Screenshot
from canvases.screenshot_factory import ScreenshotFactory


def test_creates_screenshot():
    result = ScreenshotFactory.capture()
    assert Screenshot == type(result)
