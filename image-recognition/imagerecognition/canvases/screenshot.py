from canvases.base import BaseCanvas

from PIL import Image


class Screenshot(BaseCanvas):
    def __init__(self, image: Image):
        super().__init__(image)
