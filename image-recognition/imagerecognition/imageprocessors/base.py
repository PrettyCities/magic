from typing import List

from PIL.Image import Image


class BaseImageProcessor:
    @classmethod
    def process(cls, image: Image) -> List[Image]:
        raise NotImplementedError
