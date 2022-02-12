from rdkit import Chem as Chem, RDConfig as RDConfig
from typing import Any

class FGHierarchyNode:
    children: Any
    name: str
    label: str
    pattern: Any
    smarts: str
    rxnSmarts: str
    parent: Any
    removalReaction: Any
    def __init__(self, name, patt, smarts: str = ..., label: str = ..., rxnSmarts: str = ..., parent: Any | None = ...) -> None: ...
    def __len__(self): ...

class FuncGroupFileParseError(ValueError): ...

groupDefns: Any
hierarchy: Any
lastData: Any
lastFilename: Any

def BuildFuncGroupHierarchy(fileNm: Any | None = ..., data: Any | None = ..., force: bool = ...): ...
def CreateMolFingerprint(mol, hierarchy): ...
