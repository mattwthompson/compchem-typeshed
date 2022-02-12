from rdkit import Chem as Chem
from rdkit.VLib.Output import OutputNode as BaseOutputNode
from typing import Any

class OutputNode(BaseOutputNode):
    def __init__(self, dest: Any | None = ..., delim: str = ..., idField: Any | None = ..., **kwargs) -> None: ...
    def reset(self) -> None: ...
    def smilesOut(self, mol): ...
