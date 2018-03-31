from pathlib import Path
import re
import shutil

from PIL import Image
import pytest

from imageprocessors.utils.image_saver import ImageSaver
from imageprocessors.noop import ImageNoop


class TestImageSaver:
    test_dir = Path("/tmp/imageprocessortests/test_image_saver")

    @pytest.fixture(autouse=True)
    def clean_and_create_directory(self):
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir.absolute())

        self.test_dir.mkdir(parents=True)

        yield

        shutil.rmtree(self.test_dir.absolute())

    @pytest.fixture
    def output_dir(self):
        output_dir = self.test_dir.joinpath("output")
        output_dir.mkdir()
        return output_dir

    @pytest.fixture
    def file_names(self):
        # Make test files
        file_names = ["the.png", "test.png", "names.png"]
        for fn in file_names:
            Image.new(mode="RGB", size=(1, 1)).save(
                self.test_dir.joinpath(fn).absolute()
            )
        return file_names

    @pytest.fixture
    def png_regex(self):
        return re.compile(".*\.png")

    # TODO: test_save_improper_file_extension

    def test_save(self):
        image = Image.new(mode="RGB", size=(1, 1))
        new_file_name = "test_save.png"
        output_location = self.test_dir.joinpath(new_file_name)
        ImageSaver.save(image=image, output_location=output_location)

        dir_items = list(self.test_dir.iterdir())
        assert len(dir_items) == 1
        assert dir_items[0].name == new_file_name

    def test_process_directory(self, output_dir, file_names, png_regex):
        processed_images = list(ImageSaver.process_directory(directory=self.test_dir, file_regex=png_regex,
                                                             imageprocessor=ImageNoop, output_location=output_dir))

        assert len(processed_images) == 3

        assert set(file_names) == set([file_name.name for file_name in processed_images])

    def test_process_directory_with_output_prefix(self, output_dir, file_names, png_regex):
        output_prefix = "test"
        processed_images = list(ImageSaver.process_directory(directory=self.test_dir, file_regex=png_regex,
                                                             imageprocessor=ImageNoop, output_location=output_dir,
                                                             output_prefix=output_prefix))

        assert len(processed_images) == 3

        expected = [
            "{p}{n}.png".format(p=output_prefix, n=n)
            for n in range(3)
        ]

        assert set(expected) == set([file_name.name for file_name in processed_images])
