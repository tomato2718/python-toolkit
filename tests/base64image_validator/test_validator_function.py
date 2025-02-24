from base64 import b64decode

from base64image_decoder._validator_function import (
    is_jpg,
    is_png,
)

from ._base64_image import BASE64_JPG, BASE64_PNG

JPG = b64decode(BASE64_JPG)
PNG = b64decode(BASE64_PNG)


def test_is_jpg_givenJPG_returnTrue() -> None:
    assert is_jpg(JPG) is True


def test_is_jpg_givenNoneJPG_returnFalse() -> None:
    assert is_jpg(PNG) is False


def test_is_png_givenPNG_returnTrue() -> None:
    assert is_png(PNG) is True


def test_is_png_givenNonePNG_returnFalse() -> None:
    assert is_png(JPG) is False
