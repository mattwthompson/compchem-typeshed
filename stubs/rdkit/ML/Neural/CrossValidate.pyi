from rdkit.ML.Data import SplitData as SplitData
from rdkit.ML.Neural import Network as Network, Trainers as Trainers
from typing import Any

def CrossValidate(net, testExamples, tolerance, appendExamples: int = ...): ...
def CrossValidationDriver(examples, attrs=..., nPossibleVals=..., holdOutFrac: float = ..., silent: int = ..., tolerance: float = ..., calcTotalError: int = ..., hiddenSizes: Any | None = ..., **kwargs): ...