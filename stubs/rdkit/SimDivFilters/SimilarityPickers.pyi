from rdkit import DataStructs as DataStructs
from rdkit.DataStructs.TopNContainer import TopNContainer as TopNContainer
from typing import Any

class GenericPicker:
    def MakePicks(self, force: bool = ...) -> None: ...
    def __len__(self): ...
    def __getitem__(self, which): ...

class TopNOverallPicker(GenericPicker):
    numToPick: Any
    probes: Any
    data: Any
    simMetric: Any
    def __init__(self, numToPick: int = ..., probeFps: Any | None = ..., dataSet: Any | None = ..., simMetric=...) -> None: ...
    def MakePicks(self, force: bool = ...) -> None: ...

class SpreadPicker(GenericPicker):
    numToPick: Any
    probes: Any
    data: Any
    simMetric: Any
    expectPickles: Any
    onlyNames: Any
    def __init__(self, numToPick: int = ..., probeFps: Any | None = ..., dataSet: Any | None = ..., simMetric=..., expectPickles: bool = ..., onlyNames: bool = ...) -> None: ...
    def MakePicks(self, force: bool = ..., silent: bool = ...) -> None: ...
