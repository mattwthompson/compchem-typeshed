from rdkit.VLib.Node import VLibNode as VLibNode
from typing import Any

class OutputNode(VLibNode):
    def __init__(self, dest: Any | None = ..., strFunc: Any | None = ..., **kwargs) -> None: ...
    def next(self): ...
