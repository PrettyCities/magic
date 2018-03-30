from PIL import Image

from canvases.base import BaseCanvas
from imageprocessors.utils import ImageProcessorUtils
from imageprocessors.utils import XYPixels
from imageprocessors.utils import DIRECTIONS
from resources import Resources


class MtgoTradeBoard(BaseCanvas):
    def __init__(self, image: Image):
        super().__init__(image)
        self._default_sim_thresh = 2.6

    def location_of_first_blue_post(self):
        return ImageProcessorUtils.location_of_first_occurrence(color=Resources.COLORS["blue"],
                                                                image=self.view(),
                                                                similarity_threshold=self._default_sim_thresh)

    def first_blue_row(self):
        starting_loc = self.location_of_first_blue_post()
        left = starting_loc[0]
        upper = starting_loc[1]
        right = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["blue"],
                                                        image=self.view(),
                                                        direction=DIRECTIONS.RIGHT,
                                                        starting_xy_pixels=starting_loc,
                                                        similarity_threshold=self._default_sim_thresh)
        lower = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["blue"],
                                                         image=self.view(),
                                                         direction=DIRECTIONS.BOTTOM,
                                                         starting_xy_pixels=starting_loc,
                                                         similarity_threshold=self._default_sim_thresh)
        self.view().crop((left, upper, right, lower))

    def next_white_row(self, starting_xy_pixels: XYPixels):
        starting_loc = self.location_of_first_blue_post()
        left = starting_loc[0]
        upper = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["blue"],
                                                        image=self.view(),
                                                        direction=DIRECTIONS.BOTTOM,
                                                        starting_xy_pixels=starting_loc,
                                                        similarity_threshold=self._default_sim_thresh)
        right = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["white"],
                                                        image=self.view(),
                                                        direction=DIRECTIONS.RIGHT,
                                                        starting_xy_pixels=(left, upper),
                                                        similarity_threshold=10.0)
        lower = ImageProcessorUtils.move_until_no_match(color=Resources.COLORS["white"],
                                                        image=self.view(),
                                                        direction=DIRECTIONS.BOTTOM,
                                                        starting_xy_pixels=(left, upper),
                                                        similarity_threshold=4.0)
        self.view().crop((left, upper, right, lower))
