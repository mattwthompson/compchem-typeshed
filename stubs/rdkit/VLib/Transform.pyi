from rdkit.VLib.Node import VLibNode as VLibNode
from typing import Any

class TransformNode(VLibNode):
    def __init__(self, func: Any | None = ..., **kwargs) -> None: ...
    def next(self): ...
