from pathlib import Path
from re import _pattern_type
from typing import Iterator
from typing import Type

import PIL
from PIL.Image import Image

from imageprocessors.base import BaseImageProcessor


class ImageSaver:
    @classmethod
    def save(cls, image: Image, output_location: Path) -> bool:
        # Note that this will fail if the image doesn't have a proper file extension
        image.save(output_location.absolute())
        return True

    @classmethod
    def process_directory(cls, directory: Path, file_regex: _pattern_type, imageprocessor: Type[BaseImageProcessor],
                          output_location: Path,  output_prefix: str = None) -> Iterator[Path]:
        """

        :param directory: The directory to search
        :param file_regex: The regex to run over all files in the directory to search for matches
        :param imageprocessor: The processor to run over all matched files
        :param output_location: Where to output the transformed files
        :param output_prefix: The prefix for the output file names. Defaults to found_file_name_{d++}
        :return: Iterator of all new files
        :rtype: Iterator[str]
        """
        if output_prefix:
            file_namer = lambda counter, filename: "{op}{c}".format(op=output_prefix, c=counter)
        else:
            file_namer = lambda counter, filename: "{}".format(filename)

        processed_images_counter = 0

        for file in directory.iterdir():
            match = file_regex.search(file.name)
            if match:
                image = PIL.Image.open(file)

                for processed_image in imageprocessor.process(image):
                    final_location = output_location.joinpath(
                        file_namer(processed_images_counter, file.stem)
                    ).with_suffix(file.suffix)

                    processed_image.save(final_location)

                    yield final_location.resolve()

                    processed_images_counter += 1
