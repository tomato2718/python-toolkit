from base64 import b64decode

import pytest

from base64image_decoder._decoder import (
    Base64ImageDecoder,
    ImageBytes,
)

from ._base64_image import BASE64_JPG


class MockValidatorFunction:
    received_image: ImageBytes
    __is_valid: bool

    def __init__(self, is_valid: bool) -> None:
        self.__is_valid = is_valid

    def __call__(self, image: ImageBytes) -> bool:
        self.received_image = image
        return self.__is_valid


class TestBase64ImageValidator:
    def test_givenBase64str_decodeAndValidateWithValidator(self) -> None:
        MOCK_VALIDATOR_FUNCTION = MockValidatorFunction(is_valid=True)
        decoder = Base64ImageDecoder((MOCK_VALIDATOR_FUNCTION,))

        image_bytes = decoder.decode(BASE64_JPG)

        assert (
            image_bytes
            == MOCK_VALIDATOR_FUNCTION.received_image
            == b64decode(BASE64_JPG)
        )

    def test_invalidBase64String_raiseValueError(self) -> None:
        decoder = Base64ImageDecoder([])

        with pytest.raises(ValueError):
            decoder.decode("a")

    def test_invalidImage_raiseValueError(self) -> None:
        decoder = Base64ImageDecoder((MockValidatorFunction(is_valid=False),))

        with pytest.raises(ValueError):
            decoder.decode("dGVzdA==")
