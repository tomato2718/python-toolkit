__all__ = ["Base64ImageValidator"]

from base64 import b64decode
from collections.abc import Iterable
from typing import Callable

ImageBytes = bytes
ValidatorFunction = Callable[[ImageBytes], bool]


class Base64ImageValidator:
    _validator_functions: Iterable[ValidatorFunction]

    def __init__(self, validator_functions: Iterable[ValidatorFunction]) -> None:
        self._validator_functions = validator_functions

    def validate(self, base64image: str) -> ImageBytes:
        try:
            image_bytes = b64decode(base64image)
        except Exception as e:
            raise ValueError("Input is not a valid base64 string.") from e

        if self._validator_functions and not any(
            validator(image_bytes) for validator in self._validator_functions
        ):
            raise ValueError("Input is not a valid image.")

        return image_bytes
