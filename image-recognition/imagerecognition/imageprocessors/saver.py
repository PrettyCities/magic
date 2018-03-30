from typing import List

from PIL.Image import Image

from imageprocessors.base import BaseImageProcessor


class Saver(BaseImageProcessor):
    @classmethod
    def process(cls, image: Image) -> List[Image]:
        # TODO: Configure this path
        image.save("/Users/stard/development/magic/image-recognition/imagerecognition/imageprocessors/test.png",)
        return [image]
