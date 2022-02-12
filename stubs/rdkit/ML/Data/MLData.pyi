from typing import Any

numericTypes: Any

class MLDataSet:
    data: Any
    nResults: Any
    nVars: Any
    nPts: Any
    qBounds: Any
    nPossibleVals: Any
    varNames: Any
    ptNames: Any
    def __init__(self, data, nVars: Any | None = ..., nPts: Any | None = ..., nPossibleVals: Any | None = ..., qBounds: Any | None = ..., varNames: Any | None = ..., ptNames: Any | None = ..., nResults: int = ...) -> None: ...
    def GetNResults(self): ...
    def GetNVars(self): ...
    def GetNPts(self): ...
    def GetNPossibleVals(self): ...
    def GetQuantBounds(self): ...
    def __getitem__(self, idx): ...
    def __setitem__(self, idx, val): ...
    def GetNamedData(self): ...
    def GetAllData(self): ...
    def GetInputData(self): ...
    def GetResults(self): ...
    def GetVarNames(self): ...
    def GetPtNames(self): ...
    def AddPoint(self, pt) -> None: ...
    def AddPoints(self, pts, names) -> None: ...

class MLQuantDataSet(MLDataSet):
    def GetNamedData(self): ...
    def GetAllData(self): ...
    def GetInputData(self): ...
    def GetResults(self): ...
    data: Any
    nResults: Any
    nVars: Any
    nPts: Any
    qBounds: Any
    nPossibleVals: Any
    varNames: Any
    ptNames: Any
    def __init__(self, data, nVars: Any | None = ..., nPts: Any | None = ..., nPossibleVals: Any | None = ..., qBounds: Any | None = ..., varNames: Any | None = ..., ptNames: Any | None = ..., nResults: int = ...) -> None: ...
