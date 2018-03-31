import typing

from PIL.Image import Image

from canvases.base import BaseCanvas
from imageprocessors.exceptions import ImageExhaustedException
from imageprocessors.utils.pixel_utils import ColorBox
from imageprocessors.utils.pixel_utils import PixelUtils
from imageprocessors.utils.pixel_utils import XYPixels


class MtgoTradeBoard(BaseCanvas):
    REQUIRED_IMAGE_SIZE = (1016, 625)
    # Colors
    BLUE = (194, 209, 223)
    WHITE = (233, 233, 231)

    def __init__(self, image: Image):
        super().__init__(image)
        self._default_sim_thresh = 4.0
        if self.view().size != self.REQUIRED_IMAGE_SIZE:
            raise ValueError("Images must be extracted from MtgoTradeBoard.crop_1280_960(). "
                             "Provided image was of size {}".format(self.view().size))

    @classmethod
    def crop_1280_960(cls, image: Image) -> Image:
        if image.size != (1280, 960):
            raise ValueError("Image size must be (1280, 960). The provided image was '{}'.".format(image.size))
        return image.crop((238, 167, 1254, 792))

    def _extract_color(self, starting_xy_pixels: XYPixels) -> ColorBox:
        pixel = self.view().getpixel(starting_xy_pixels)

        if PixelUtils.is_similar(pixel_one=pixel, pixel_two=self.WHITE, similarity_threshold=self._default_sim_thresh):
            return self.WHITE

        elif PixelUtils.is_similar(pixel_one=pixel, pixel_two=self.BLUE, similarity_threshold=self._default_sim_thresh):
            return self.BLUE

        else:
            raise ValueError("First pixel '{p}' is not WHITE '{w}' or BLUE '{b}'.".format(
                p=pixel, w=self.WHITE, b=self.BLUE
            ))

    def _extract_post(self, starting_xy_pixels: XYPixels) -> typing.Tuple[Image, int]:
        """
        NOTE: This assumes that the starting_xy_pixels are positioned at the very start of the post
        :param starting_xy_pixels:
        :return:
        """
        color = self._extract_color(starting_xy_pixels)

        lower = PixelUtils.move_down_until_no_match(color=color, image=self.view(),
                                                    starting_xy_pixels=starting_xy_pixels,
                                                    similarity_threshold=self._default_sim_thresh)
        left = starting_xy_pixels[0]
        upper = starting_xy_pixels[1]
        right = 1016

        return self.view().crop((left, upper, right, lower)), lower

    def extract_posts(self) -> typing.Iterator[Image]:
        starting_xy_pixels = (0, 0)
        try:
            while True:
                post, lower = self._extract_post(starting_xy_pixels)
                yield post
                starting_xy_pixels = (0, lower)
        except ImageExhaustedException:
            return
