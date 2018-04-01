from PIL import Image


class Viewable:
    def __init__(self, image: Image):
        self._image = image

    def view(self) -> Image:
        return self._image
