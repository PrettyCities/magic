from pathlib import Path

from PIL import Image
import pytest

from mixins.withcurrentdirectory import WithCurrentDirectory


@pytest.fixture
def image():
    return Image.new(mode="RGB", size=(100, 100))


@pytest.fixture
def resources_directory():
    return Path(WithCurrentDirectory.current_directory(__file__)).joinpath("resources").absolute()
