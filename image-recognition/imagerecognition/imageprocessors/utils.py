from typing import Mapping
from typing import Tuple

from PIL import Image

from utils import percent_difference

Left = int
Upper = int
Right = int
Lower = int

ColorBox = Tuple[int, int, int, int]
PixelBox = Tuple[Left, Upper, Right, Lower]
XYPixels = Tuple[int, int]


class ImageProcessorUtils:
    @classmethod
    def location_of_first_occurrence(cls, color: ColorBox, image: Image,
                                     similarity_threshold: float = 0.0) -> XYPixels:
        width = image.width
        height = image.height

        if (width == 0) or (height == 0):
            # TODO: Handle the 1x1 case
            raise ValueError("This utility function can only handle images of at least 2x2 size.")

        x = 0
        y = 0

        while (x < width) or (y < height):
            if x == width:
                # Restart, one pixel down
                x = 0
                y += 1
            pixel = image.getpixel((x, y))
            # Account for the fact that some images may have very similar colors
            # that we may want to consider as identical
            if cls.is_similar(pixel_one=pixel, pixel_two=color, similarity_threshold=similarity_threshold):
                return x, y
            else:
                if x < width:
                    # Move one pixel to the right
                    x += 1

        # TODO: Exception?
        return None

    @classmethod
    def is_similar(cls, pixel_one: ColorBox, pixel_two: ColorBox, similarity_threshold: float) -> bool:
        both_boxes = zip(pixel_one, pixel_two)
        differences = map(percent_difference, both_boxes)
        max_diff = max(differences)
        if max_diff <= similarity_threshold:
            return True
        else:
            return False

    @classmethod
    def right_until_no_match(cls, color: ColorBox, image: Image, starting_xy_pixels: XYPixels = (0, 0),
                             similarity_threshold: float = 0.0) -> Right:
        width = image.width
        x = starting_xy_pixels[0]
        y = starting_xy_pixels[1]

        # Move one pixel to the right to start
        y += 1

        while y < width:
            pixel = image.getpixel((x, y))
            if not cls.is_similar(pixel_one=pixel, pixel_two=color, similarity_threshold=similarity_threshold):
                return y
            y += 1
        # TODO: Exception?
        # Only matches found
        return None

    @classmethod
    def move_right_until_no_match(cls, color: ColorBox, image: Image, starting_xy_pixels: XYPixels = (0, 0),
                                  similarity_threshold: float = 0.0) -> int:
        x = starting_xy_pixels[0]
        y = starting_xy_pixels[1]

        width = image.width

        x += 1

        while x <= width:
            pixel = image.getpixel((x, y))
            if not cls.is_similar(pixel_one=pixel, pixel_two=color, similarity_threshold=similarity_threshold):
                return pixel
            else:
                x += 1

        return None

    @classmethod
    def move_left_until_no_match(cls, color: ColorBox, image: Image, starting_xy_pixels: XYPixels = (0, 0),
                                  similarity_threshold: float = 0.0) -> int:
        x = starting_xy_pixels[0]
        y = starting_xy_pixels[1]

        width = image.width

        x -= 1

        while x >= width:
            pixel = image.getpixel((x, y))
            if not cls.is_similar(pixel_one=pixel, pixel_two=color, similarity_threshold=similarity_threshold):
                return pixel
            else:
                x -= 1

        return None

    @classmethod
    def move_down_until_no_match(cls, color: ColorBox, image: Image, starting_xy_pixels: XYPixels = (0, 0),
                                  similarity_threshold: float = 0.0) -> int:
        x = starting_xy_pixels[0]
        y = starting_xy_pixels[1]

        y -= 1

        while y <= 0:
            pixel = image.getpixel((x, y))
            if not cls.is_similar(pixel_one=pixel, pixel_two=color, similarity_threshold=similarity_threshold):
                return pixel
            else:
                y -= 1

        return None

    @classmethod
    def move_up_until_no_match(cls, color: ColorBox, image: Image, starting_xy_pixels: XYPixels = (0, 0),
                                  similarity_threshold: float = 0.0) -> int:
        x = starting_xy_pixels[0]
        y = starting_xy_pixels[1]

        height = image.height

        y += 1

        while y <= height:
            pixel = image.getpixel((x, y))
            if not cls.is_similar(pixel_one=pixel, pixel_two=color, similarity_threshold=similarity_threshold):
                return pixel
            else:
                y += 1

        return None


    @classmethod
    def move_until_no_match(cls, color: ColorBox, image: Image, direction: Mapping[str, str],
                            starting_xy_pixels: XYPixels = (0, 0), similarity_threshold: float = 0.0) -> int:
        if direction["pixel"] == "x":
            x = True
            moving_pixel = starting_xy_pixels[0]
            stationary_pixel = starting_xy_pixels[1]
            bound = image.width
        else:
            x = False
            moving_pixel = starting_xy_pixels[1]
            stationary_pixel = starting_xy_pixels[0]
            bound = image.height

        comparison = direction["comparison"]
        num_modifier = direction["num_modifier"]

        # Move one pixel to start
        moving_pixel = moving_pixel.__getattribute__(num_modifier)(1)

        while moving_pixel.__getattribute__(comparison)(bound):
            if x:
                pixel_to_get = (moving_pixel, stationary_pixel)
            else:
                pixel_to_get = (stationary_pixel, moving_pixel)

            pixel = image.getpixel(pixel_to_get)
            if not cls.is_similar(pixel_one=pixel, pixel_two=color, similarity_threshold=similarity_threshold):
                return moving_pixel

            moving_pixel = moving_pixel.__getattribute__(num_modifier)(1)
        # TODO: Exception?
        # Only matches found
        return None


# TODO: Decide if we even want to keep this considering preferring directional methods to the abstract
class _DIRECTIONS:
    _NO_MATCH_MAPPINGS = {
        "right": {
            "pixel": "x", "comparison": "__lt__", "num_modifier": "__add__",
        },
        "left": {
            "pixel": "x", "comparison": "__gt__", "num_modifier": "__sub__",
        },
        "bottom": {
            "pixel": "y", "comparison": "__lt__", "num_modifier": "__add__",
        },
        "top": {
            "pixel": "y", "comparison": "__gt__", "num_modifier": "__sub__",
        },
    }

    @property
    def RIGHT(self):
        return self._NO_MATCH_MAPPINGS["right"]

    @property
    def LEFT(self):
        return self._NO_MATCH_MAPPINGS["left"]

    @property
    def BOTTOM(self):
        return self._NO_MATCH_MAPPINGS["bottom"]

    @property
    def TOP(self):
        return self._NO_MATCH_MAPPINGS["top"]

DIRECTIONS = _DIRECTIONS()