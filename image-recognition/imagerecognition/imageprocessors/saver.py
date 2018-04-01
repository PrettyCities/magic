from typing import Iterator

from PIL.Image import Image

from imageprocessors.base import BaseImageProcessor


class Saver(BaseImageProcessor):
    @classmethod
    def process(cls, image: Image) -> Iterator[Image]:
        # TODO: Configure this path
        image.save("/Users/stard/development/magic/image-recognition/imagerecognition/imageprocessors/test.png",)
        yield Image
