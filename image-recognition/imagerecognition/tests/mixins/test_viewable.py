from mixins.viewable import Viewable


def test_has_image(image):
    klass = Viewable(image=image)
    assert klass.view() == image

