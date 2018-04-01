from typing import Iterator

from PIL.Image import Image

from imageprocessors.base import BaseImageProcessor


class ImageNoop(BaseImageProcessor):
    """
    Used for testing
    """
    @classmethod
    def process(cls, image: Image) -> Iterator[Image]:
        yield image
