from typing import Callable
from typing import Iterator
from typing import Type

from PIL.Image import Image

from imageprocessors.base import BaseImageProcessor


class WrapAsProcessor:
    @classmethod
    def wrap(cls, _callable: Callable[[Type[object], Image], Iterator[Image]]) -> Type[BaseImageProcessor]:
        class Wrapped(BaseImageProcessor):
            @classmethod
            def process(cls, image: Image) -> Iterator[Image]:
                # NOTE: Intellij sees this as a type issue, but it isn't because python will pass the object implicitly.
                return _callable(image)

        return Wrapped
