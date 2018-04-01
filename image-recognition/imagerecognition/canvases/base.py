from PIL import Image

from mixins.viewable import Viewable


class BaseCanvas(Viewable):
    def __init__(self, image: Image):
        super().__init__(image)
