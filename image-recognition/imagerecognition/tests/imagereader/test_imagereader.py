from PIL import Image
from pathlib import Path

from imagereader.base import ImageReader


def test_read(resources_directory: Path):
    path = resources_directory.joinpath("imagereader").joinpath("hello.jpg")
    image = Image.open(path)
    expected = "Hello."
    result = ImageReader.read(image=image)
    assert expected == result
