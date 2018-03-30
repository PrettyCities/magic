from canvases.base import BaseCanvas

from PIL import Image


class PriceRow(BaseCanvas):
    def __init__(self, image: Image):
        super().__init__(image)

    @property
    def prices(self):
        # TODO:
        # - Tesseract
        # - Parse results
        # - Return list Price objects (card name and row)
        raise NotImplementedError
