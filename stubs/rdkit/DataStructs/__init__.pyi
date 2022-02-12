from rdkit.DataStructs.cDataStructs import *
from rdkit import rdBase as rdBase
from rdkit.DataStructs import cDataStructs as cDataStructs
from typing import Any

__doc__: Any
similarityFunctions: Any

def FingerprintSimilarity(fp1, fp2, metric=...): ...
def FoldToTargetDensity(fp, density: float = ..., minLength: int = ...): ...
