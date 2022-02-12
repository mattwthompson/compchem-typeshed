from rdkit.ML.KNN import KNNModel as KNNModel
from typing import Any

class KNNRegressionModel(KNNModel.KNNModel):
    def __init__(self, k, attrs, dfunc, radius: Any | None = ...) -> None: ...
    def type(self): ...
    def SetBadExamples(self, examples) -> None: ...
    def GetBadExamples(self): ...
    def NameModel(self, varNames) -> None: ...
    def PredictExample(self, example, appendExamples: int = ..., weightedAverage: int = ..., neighborList: Any | None = ...): ...