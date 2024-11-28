__all__ = ["is_jpg", "is_png"]

_JPG_SIGNATURE = bytes.fromhex("ffd8ff")
_PNG_SIGNATURE = bytes.fromhex("89504e470d0a1a0a")


def is_jpg(image_bytes: bytes) -> bool:
    return image_bytes[:3] == _JPG_SIGNATURE


def is_png(image_bytes: bytes) -> bool:
    return image_bytes[:8] == _PNG_SIGNATURE
