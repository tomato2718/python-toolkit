__all__ = ["SnowflakeIDGenerator"]

from threading import Lock
from typing import Callable


class SnowflakeIDGenerator:
    """
    This class will generate a 64-bit ID in the following format:

    ``32-bit timestamp | 16-bit Node ID | 16-bit Node Sequence Number``
    """

    _node_id: int
    _get_timestamp: Callable[[], int]
    _last_call: int
    _count: int
    _lock: Lock

    def __init__(
        self,
        *,
        node_id: int,
        timestamp_generator: Callable[[], int],
    ) -> None:
        """
        :param int node_id: 16-bit node ID, will be masked if it overflows.
        :param func timestamp_generator: A callable that returns a timestamp in seconds.
        """
        self._node_id = node_id & 0xFFFF
        self._get_timestamp = timestamp_generator
        self._last_call = 0
        self._count = 0
        self._lock = Lock()

    def __call__(self) -> bytes:
        with self._lock:
            now = self._get_timestamp()
            if now != self._last_call:
                self._count = 0
            self._count = (self._count + 1) & 0xFFFF
            self._last_call = now
            id = now << 32 | self._node_id << 16 | self._count
        return id.to_bytes(length=8, byteorder="big")
