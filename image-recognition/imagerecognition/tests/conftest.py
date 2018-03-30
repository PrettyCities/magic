from PIL import Image
import pytest

from resources import Resources


@pytest.fixture
def hello():
    return Resources.hello()


@pytest.fixture
def image():
    return Image.new(mode="RGB", size=(100, 100))
