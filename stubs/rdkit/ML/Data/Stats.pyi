from typing import Any

def StandardizeMatrix(mat): ...
def FormCovarianceMatrix(mat): ...
def FormCorrelationMatrix(mat): ...
def PrincipalComponents(mat, reverseOrder: int = ...): ...
def TransformPoints(tFormMat, pts): ...
def MeanAndDev(vect, sampleSD: int = ...): ...
def R2(orig, residSum): ...

tConfs: Any
tTable: Any

def GetConfidenceInterval(sd, n, level: int = ...): ...
