from rdkit import Chem as Chem
from rdkit.Chem.Pharm2D import Utils as Utils
from typing import Any

class MatchError(Exception): ...

def GetAtomsMatchingBit(sigFactory, bitIdx, mol, dMat: Any | None = ..., justOne: int = ..., matchingAtoms: Any | None = ...): ...
