from rdkit.ML.Data import DataUtils as DataUtils
from typing import Any

class Composite:
    modelList: Any
    errList: Any
    countList: Any
    modelVotes: Any
    quantBounds: Any
    nPossibleVals: Any
    quantizationRequirements: Any
    activityQuant: Any
    def __init__(self) -> None: ...
    def SetModelFilterData(self, modelFilterFrac: float = ..., modelFilterVal: float = ...) -> None: ...
    def SetDescriptorNames(self, names) -> None: ...
    def GetDescriptorNames(self): ...
    def SetQuantBounds(self, qBounds, nPossible: Any | None = ...) -> None: ...
    def GetQuantBounds(self): ...
    def GetActivityQuantBounds(self): ...
    def SetActivityQuantBounds(self, bounds) -> None: ...
    def QuantizeActivity(self, example, activityQuant: Any | None = ..., actCol: int = ...): ...
    def QuantizeExample(self, example, quantBounds: Any | None = ...): ...
    def MakeHistogram(self): ...
    def CollectVotes(self, example, quantExample, appendExample: int = ..., onlyModels: Any | None = ...): ...
    def ClassifyExample(self, example, threshold: int = ..., appendExample: int = ..., onlyModels: Any | None = ...): ...
    def GetVoteDetails(self): ...
    def GetInputOrder(self): ...
    def SetInputOrder(self, colNames) -> None: ...
    def Grow(self, examples, attrs, nPossibleVals, buildDriver, pruner: Any | None = ..., nTries: int = ..., pruneIt: int = ..., needsQuantization: int = ..., progressCallback: Any | None = ..., **buildArgs) -> None: ...
    def ClearModelExamples(self) -> None: ...
    def Pickle(self, fileName: str = ..., saveExamples: int = ...) -> None: ...
    def AddModel(self, model, error, needsQuantization: int = ...) -> None: ...
    def AverageErrors(self): ...
    def SortModels(self, sortOnError: bool = ...) -> None: ...
    def GetModel(self, i): ...
    def SetModel(self, i, val) -> None: ...
    def GetCount(self, i): ...
    def SetCount(self, i, val) -> None: ...
    def GetError(self, i): ...
    def SetError(self, i, val) -> None: ...
    def GetDataTuple(self, i): ...
    def SetDataTuple(self, i, tup) -> None: ...
    def GetAllData(self): ...
    def __len__(self): ...
    def __getitem__(self, which): ...
