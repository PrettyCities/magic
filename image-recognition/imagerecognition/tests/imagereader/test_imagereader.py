from imagereader.base import ImageReader


def test_read(hello):
    expected = "Hello."
    result = ImageReader.read(image=hello)
    assert expected == result
