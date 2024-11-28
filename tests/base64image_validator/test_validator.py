from base64 import b64decode

import pytest

from base64image_validator._validator import (
    Base64ImageValidator,
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
        validator = Base64ImageValidator((MOCK_VALIDATOR_FUNCTION,))

        image_bytes = validator.validate(BASE64_JPG)

        assert (
            image_bytes
            == MOCK_VALIDATOR_FUNCTION.received_image
            == b64decode(BASE64_JPG)
        )

    def test_invalidBase64String_raiseValueError(self) -> None:
        validator = Base64ImageValidator([])

        with pytest.raises(ValueError):
            validator.validate("a")

    def test_invalidImage_raiseValueError(self) -> None:
        validator = Base64ImageValidator((MockValidatorFunction(is_valid=False),))

        with pytest.raises(ValueError):
            validator.validate("dGVzdA==")
