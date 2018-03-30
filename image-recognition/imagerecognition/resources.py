from PIL import Image
from pathlib import Path

from mixins.withcurrentdirectory import WithCurrentDirectory


class Resources(WithCurrentDirectory):
    COLORS = {
        "blue": (194, 209, 223, 255),
        "white": (233, 233, 231, 255)
    }

    @classmethod
    def hello(cls):
        return Image.open(Path("{cwd}/tests/resources/hello.jpg".format(
            cwd=cls.current_directory(__file__)))
        )

    @classmethod
    def firstblue_1(cls):
        return Image.open(Path("{cwd}/tests/resources/tradecolors/firstblue_1.png".format(
                    cwd=cls.current_directory(__file__))))

    @classmethod
    def firstblue_2(cls):
        return Image.open(Path("{cwd}/tests/resources/tradecolors/firstblue_2.png".format(
            cwd=cls.current_directory(__file__))))

    @classmethod
    def lastblue_1(cls):
        return Image.open(Path("{cwd}/tests/resources/tradecolors/lastblue_1.png".format(
            cwd=cls.current_directory(__file__))))

    @classmethod
    def lastblue_2(cls):
        return Image.open(Path("{cwd}/tests/resources/tradecolors/lastblue_2.png".format(
            cwd=cls.current_directory(__file__))))

    @classmethod
    def bluefromposting_1(cls):
        return Image.open(Path("{cwd}/tests/resources/tradecolors/bluefromposting_1.png".format(
            cwd=cls.current_directory(__file__))))

    @classmethod
    def bluefromposting_2(cls):
        return Image.open(Path("{cwd}/tests/resources/tradecolors/bluefromposting_2.png".format(
            cwd=cls.current_directory(__file__))))

    @classmethod
    def mtgotraderboard(cls):
        return Image.open(Path("{cwd}/tests/resources/mtgotradeboard.png".format(
            cwd=cls.current_directory(__file__))))

    @classmethod
    def blue_images(cls):
        return [
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/firstblue_1.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0),
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/lastblue_1.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/firstblue_2.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0),
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/lastblue_2.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/bluefromposting_1.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (18, 8)
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/bluefromposting_2.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (12, 6)
            }
        ]

    @classmethod
    def white_images(cls):
        return [
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/firstwhite_1.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/lastwhite_1.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/firstwhite_2.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/lastwhite_2.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 0)
            },
            {
                "image": Image.open(Path("{cwd}/tests/resources/tradecolors/whitefromposting_1.png".format(
                    cwd=cls.current_directory(__file__)))
                ),
                "expected_location": (0, 1)
            }
            # NOTE: This image does not work because the side bar is the same color white.
            # When writing the app, we will need to chop out the section of the screen
            # that contains the postings before splitting again by similarity.
            # {
            #     "image": Image.open(Path("{cwd}/tests/resources/tradecolors/whitefromposting_2.png".format(
            #         cwd=cls.current_directory(__file__)))
            #     ),
            #     "expected_location": (18, 8)
            # }
        ]
