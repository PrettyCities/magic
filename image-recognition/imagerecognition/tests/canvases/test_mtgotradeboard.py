from pathlib import Path

from PIL import Image
import pytest

from canvases.mtgotradeboard import MtgoTradeBoard


class TestMtgoTradeBoard:
    @pytest.fixture()
    def trade_board(self, resources_directory: Path):
        board = resources_directory.joinpath("canvases").joinpath("tradeboard_1.png")
        image = Image.open(board.absolute())
        return MtgoTradeBoard(image)

    def test_crop_1280_960(self, resources_directory: Path):
        rawboard = resources_directory.joinpath("canvases").joinpath("rawboard.png")
        image = Image.open(rawboard.absolute())
        cropped_board = MtgoTradeBoard.crop_1280_960(image)

        assert cropped_board.size == MtgoTradeBoard.REQUIRED_IMAGE_SIZE

    def test_crop_1280_960_bad_arg(self, resources_directory: Path):
        bad_size_image = resources_directory.joinpath("imagereader").joinpath("hello.jpg")
        image = Image.open(bad_size_image)
        with pytest.raises(ValueError):
            MtgoTradeBoard.crop_1280_960(image)

    def test__extract_color(self, trade_board: MtgoTradeBoard):
        first = (0, 0)
        first_color = trade_board._extract_color(starting_xy_pixels=first)
        assert MtgoTradeBoard.BLUE == first_color

        second = (0, 42)
        second_color = trade_board._extract_color(starting_xy_pixels=second)
        assert MtgoTradeBoard.WHITE == second_color

        third = (0, 83)
        third_color = trade_board._extract_color(starting_xy_pixels=third)
        assert MtgoTradeBoard.BLUE == third_color

    def test__extract_post(self, trade_board: MtgoTradeBoard):
        first = (0, 0)
        first_post, first_next_y = trade_board._extract_post(starting_xy_pixels=first)
        assert first_post.width == MtgoTradeBoard.REQUIRED_IMAGE_SIZE[0]
        assert first_next_y == 42

        second = (0, 42)
        second_post, second_next_y = trade_board._extract_post(starting_xy_pixels=second)
        assert second_post.width == MtgoTradeBoard.REQUIRED_IMAGE_SIZE[0]
        assert second_next_y == 83

        third = (0, 83)
        third_post, third_next_y = trade_board._extract_post(starting_xy_pixels=third)
        assert third_post.width == MtgoTradeBoard.REQUIRED_IMAGE_SIZE[0]
        assert third_next_y == 125

    def test_extract_posts(self, trade_board: MtgoTradeBoard):
        posts = list(trade_board.extract_posts())

        assert 15 == len(posts)

        for post in posts:
            assert post.width == MtgoTradeBoard.REQUIRED_IMAGE_SIZE[0]
            assert 38 <= post.height <= 42
