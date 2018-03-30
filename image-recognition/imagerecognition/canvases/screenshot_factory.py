from PIL import ImageGrab

from canvases.screenshot import Screenshot


class ScreenshotFactory:
    @classmethod
    def capture(cls):
        image = ImageGrab.grab()
        return Screenshot(image=image)
