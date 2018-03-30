from typing import List

from PIL.Image import Image

from canvases.base import BaseCanvas
from canvases.price_row import PriceRow
from imageprocessors.base import BaseImageProcessor
from imageprocessors.utils import ImageProcessorUtils


class PriceRowExtractor(BaseImageProcessor):
    lightblue = (194, 209, 223, 255)

    @classmethod
    def process(cls, image: BaseCanvas) -> List[BaseCanvas]:
        return [
            PriceRow(image=price_image) for price_image in cls._find_price_rows(image)
        ]

    @classmethod
    def _find_price_rows(cls, image: BaseCanvas) -> List[Image]:
        # Find light blue pixel color
        location = ImageProcessorUtils.location_of_first_occurrence(color=cls.lightblue, image=image)
        # Create bands around each light blue color
        pass
