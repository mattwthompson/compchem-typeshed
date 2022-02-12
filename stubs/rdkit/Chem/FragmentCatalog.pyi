from rdkit.Chem.rdfragcatalog import *
from rdkit import Chem as Chem
from typing import Any

def message(msg, dest=...) -> None: ...

class BitGainsInfo:
    id: int
    description: str
    gain: float
    nPerClass: Any

def ProcessGainsFile(fileName, nToDo: int = ..., delim: str = ..., haveDescriptions: int = ...): ...
def BuildAdjacencyList(catalog, bits, limitInclusion: int = ..., orderLevels: int = ...): ...
def GetMolsMatchingBit(mols, bit, fps): ...
