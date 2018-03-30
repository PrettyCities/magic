from typing import List

from PIL.Image import Image

from imageprocessors.base import BaseImageProcessor
from utils import BoxFactory


class ImageHalver(BaseImageProcessor):
    @classmethod
    def process(cls, image: Image) -> List[Image]:
        height = image.height
        width = image.width

        tophalf = BoxFactory.make(left=0, upper=0, right=width, lower=height / 2)
        bottomhalf = BoxFactory.make(left=0, upper=height / 2, right=width, lower=height)

        return [image.crop(box=tophalf), image.crop(box=bottomhalf)]
