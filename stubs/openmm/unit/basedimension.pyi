from typing import Any

class BaseDimension:
    name: Any
    def __init__(self, name) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
