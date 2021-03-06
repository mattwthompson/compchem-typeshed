from rdkit import RDConfig as RDConfig
from rdkit.VLib.Supply import SupplyNode as SupplyNode
from typing import Any

class _lazyDataSeq:
    cursor: Any
    cmd: Any
    def __init__(self, cursor, cmd, pickleCol: int = ..., depickle: int = ..., klass: Any | None = ...) -> None: ...
    def __iter__(self): ...
    def next(self): ...

class _dataSeq(_lazyDataSeq):
    cursor: Any
    cmd: Any
    res: Any
    rowCount: int
    idx: int
    def __init__(self, cursor, cmd, pickleCol: int = ..., depickle: int = ...) -> None: ...
    def __iter__(self): ...
    def next(self): ...
    def __len__(self): ...
    def __getitem__(self, idx): ...

class DbPickleSupplyNode(SupplyNode):
    def __init__(self, cursor, cmd, binaryCol, **kwargs) -> None: ...
    def reset(self) -> None: ...
    def next(self): ...

def GetNode(dbName, tableName): ...
