from typing import Any

class LazySig:
    computeFunc: Any
    size: Any
    def __init__(self, computeFunc, sigSize) -> None: ...
    def __len__(self): ...
    def __getitem__(self, which): ...
