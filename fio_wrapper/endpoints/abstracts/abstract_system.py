from typing import Optional


class AbstractSystem:
    def get(self, planet: str, timeout: Optional[float] = None):
        raise NotImplementedError()

    def all(self, timeout: Optional[float] = None):
        raise NotImplementedError()
