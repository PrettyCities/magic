from typing import Iterator

from PIL.Image import Image


class BaseImageProcessor:
    @classmethod
    def process(cls, image: Image) -> Iterator[Image]:
        raise NotImplementedError
